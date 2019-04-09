import matplotlib
matplotlib.use('agg')
import argparse
import numpy as np
import os, os.path as osp

import sys
sys.path.insert(0, '/home/hale/caffe/segflow-caffe/python')
import caffe
from caffe.proto import caffe_pb2
from google.protobuf import text_format

def inference(args):

    # get Python layer from test prototxt
    model_obj = caffe_pb2.NetParameter()
    text_format.Merge(open(args.proto).read(), model_obj)

    assert model_obj.layer[0].type == 'Python', \
        'First layer is not Python layer, model '+args.model

    # get input blobs and param_str
    in_blobs = list(model_obj.layer[0].top)
    params = eval(model_obj.layer[0].python_param.param_str)
    paths = dict((t, open(params[t+'-path']).read().splitlines())
            for t in in_blobs if 'img_idx' not in t)
    k = paths.keys()[0]
    n = len(paths[k])
    for t in paths:
        assert len(paths[t]) == n, \
        'Lengths mismatch for {} and {}: {:d} vs. {:d}'.format(k, t, n, len(paths[t]))

    # forward an image through given net and save labelled results to files
    print 'Running net inference'

    # create the test net
    caffe.set_mode_gpu()
    caffe.set_device(args.gpu)
    net = caffe.Net(args.proto, args.weight, caffe.TEST)

    for i in range(n):
        net.forward()
        id = int(net.blobs['img_idx'].data[0])
        blobs = dict()
        for b in in_blobs+args.out_blobs:
            path = paths[b][id] if b in paths else ''
            blobs[b] = (path, net.blobs[b].data) if 'img_idx' not in b else id
        yield blobs


def save_to_file(path, pr, modality, sample=None):

    import flow # to convert flow to RGB
    from PIL import Image
    import matplotlib.pyplot as plt
    import scipy.io as sio

    if not osp.exists(osp.dirname(path)):
        os.makedirs(osp.dirname(path))
        print 'Creating output dir', osp.dirname(path)

    if 'seg' in modality:
        if sample is not None:
            s = Image.open(sample)
            palette = s.getpalette()
        else:
            norm = plt.Normalize(vmin=0, vmax=40)
            palette = list(sum([plt.cm.Paired(norm(i))[:3] for i in range(0, 255)],()))
            palette = [int(x * 255) for x in palette]
        im = Image.fromarray(pr.astype(np.uint8), mode='P')
        im.putpalette(palette)
    elif 'flow' in modality:
        flow.flow_write(path, pr)
        # visualization
        im = Image.fromarray(flow.to_color(pr))
        path = path + '_vis.png'
    elif 'norm' in modality:
        sio.savemat(path, {'normal': pr})
        im = pr / np.sqrt(np.power(pr, 2).sum(axis=2, keepdims=True))
        im = Image.fromarray(im.astype(np.uint8))
        path = path + '_vis.png'
    elif 'depth' in modality:
        sio.savemat(path, {'depth': pr})
        cmap = plt.cm.jet # use a simple color map
        norm = plt.Normalize(vmin=0, vmax=200) #anno.max())
        im = Image.fromarray(cmap(norm(pr)))
        path = path + '_vis.png'

    im.save(path)

def no_eval(args):
    pass

def evaluate(args):
    import yaml
    import evaluator

    pinfo = yaml.load(open(args.config))
    xinfo = yaml.load(open(args.exp))
    dinfo = yaml.load(open(osp.join(
                            pinfo['PROJECT']['ROOT'],
                            pinfo['PROJECT']['CONFIG'],
                            xinfo['INPUT']['DATASET'])))

    nclasses = dinfo['seg']['n']
    void_label = dinfo['seg']['ignore_label']
    mapping = None
    if 'mapping' in dinfo['seg']:
        mapping = dinfo['seg']['mapping']
        mapping = dict(zip(mapping, xrange(len(mapping))))

    evaluators = {'seg': evaluator.Seg(nclasses, void_label),
            'flow': evaluator.Flow(),
            'norm': evaluator.Norm()}

    counter = 0
    print 'Processing files...'
    for infr in inference(args):

        counter += 1

        for modality in ['seg', 'norm', 'flow']:

            gt_dict = None
            pr_dict = None

            for k in infr:
                if modality not in k:
                    continue
                if 'gt' in k:
                    gt_dict = {'path': infr[k][0], 'data': infr[k][1]}
                if k in args.out_blobs:
                    pr_dict = {'path': infr[k][0], 'data': infr[k][1]}

            if gt_dict is None or pr_dict is None:
                continue

            pr_dict['path'] = osp.join(args.outdir, gt_dict['path'].replace('/', '_'))
            (pr, gt) = evaluators[modality].eval_perimg(pr_dict, gt_dict)
            save_to_file(pr_dict['path'], pr, modality, args.palette)
            print str(counter) + ' | ', pr_dict['path']

    # TODO: report
    # confusion matrices
    # results
    # few examples

    exp = os.path.basename(args.exp).split('.')[0]

    from datetime import datetime as dt
    report_txt = '\n\n---------\n### Testing network'
    report_txt += '\n- *date* : ' + str(dt.today().strftime("%d-%m-%Y"))
    report_txt += ' | *time* : ' + str(dt.now().strftime("%H:%M:%S"))
    report_txt += '\n- *experiment* : ' + exp
    for arg in vars(args):
        report_txt += '\n- *{:s}* : {:s}'.format(arg, str(getattr(args, arg)))

    open(args.report, 'a').write(report_txt + '\n'*2)

    for e in evaluators:
        a = evaluators[e].eval_all()
        if a is not None:
            if args.report is not None:
                report = evaluators[e].report_all()
                with open(args.report, 'a') as f:
                    f.write(report)
                    evaluators[e].extra_report(osp.dirname(args.report), f)
            if args.perimg is not None:
                open(args.perimg, 'w').write(evaluators[e].report_perimg())
            if args.common is not None:
                open(args.common, 'a').write(exp + ' | ' + report.split('\n')[2] + '\n')

def main():
    # Import arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True)
    parser.add_argument('--exp', type=str, required=True)
    parser.add_argument('--proto', type=str, required=True)
    parser.add_argument('--weight', type=str, required=True)
    parser.add_argument('--outdir', type=str, required=True)
    parser.add_argument('--out_blobs', nargs='+', required=True,
            help='List of output blobs by the network separated by spaces')
    parser.add_argument('--gpu', type=str, required=False, default=0)

    parser.add_argument('--palette', type=str, required=False, default=None,
            help='Path to a ground truth segmentation that has palette information')

    parser.add_argument('--perimg', type=str, required=False, default=None,
            help='Path to per image report')
    parser.add_argument('--report', type=str, required=False, default=None,
            help='Path to result report')
    parser.add_argument('--common', type=str, required=False, default=None,
            help='Path to common report file for all experiments')


    #parser.add_argument('--mapping', type=str, required=False) # from mappings.py
    #parser.add_argument('--nclasses', type=int, required=False) # from mappings.py
    #parser.add_argument('--novisualize', type=bool, required=False)
    #parser.add_argument('--resultfile', type=str, required=False)
    #parser.add_argument('--rawmapping', type=int, required=False)
    #parser.add_argument('--do-eval', dest='do_eval', action='store_true', required=False)
    #parser.add_argument('--no-eval', dest='do_eval', action='store_false', required=False)
    #parser.set_defaults(do_eval=True)
    #parser.add_argument('--do-forward', dest='forward', action='store_true', required=False)
    #parser.add_argument('--no-forward', dest='forward', action='store_false', required=False)
    #parser.set_defaults(forward=True)
    #parser.add_argument('--do-per-img', dest='per_img', action='store_true', required=False)
    #parser.add_argument('--no-per-img', dest='per_img', action='store_false', required=False)
    #parser.set_defaults(per_img=True) # TODO set this to FALSE
    #parser.add_argument('--do-save-inp', dest='save_inp', action='store_true', required=False)
    #parser.add_argument('--no-save-inp', dest='save_inp', action='store_false', required=False)
    #parser.set_defaults(save_inp=True) # TODO set this to FALSE
    ## TODO: if input layer is not python (e.g. LMDB), we need to read the list of
    ## input modality separately
    #parser.add_argument('--is_deploy', dest='is_deploy', action='store_true', required=False, default=False)
    #parser.add_argument('--list_file', type=str, required=False)
    #parser.set_defaults(save_inp=True) # TODO set this to FALSE
    args = parser.parse_args()

    evaluate(args)


main()
