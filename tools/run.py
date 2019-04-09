# system packages
import re
import yaml
import argparse
import os, os.path as osp

# project packages
import arch
import get_class_weights as gcw


from subprocess import call


def create_net(args):
    """
        Read and parse net config from file and pass the parameter to arch to generate net
    """

    # Load config file for this experiment
    xinfo = yaml.load(open(args.exp)) # experiment info

    # copy config to run directory
    assert osp.isdir(args.cache_dir), 'Working directory not found: ' + args.cache_dir
    # output config file
    yaml.dump(xinfo, open(args.exp_config_path, 'w'),
            default_flow_style=False)

    # Load dataset config file
    dcfg_path = osp.join(args.data_config_path, xinfo['INPUT']['DATASET'])
    dinfo = yaml.load(open(dcfg_path)) # dataset info
    data_dir = dinfo['ROOT']

    layout = xinfo['INPUT']['LAYOUT']
    inps = [s.strip() for l in layout for s in l.split(',')]
    outs = [s.strip() for s in xinfo['REFINE']['TARGETS'].split(',')]

    supports = ['seg', 'flow', 'norm', 'rgb', 'depth']

    nets = {}
    for split in ['train', 'test']:
        net_inps = []
        net_outs = []
        for inp in inps:
            match = re.search('^(gt|pr)({})'.format('|'.join(supports)), inp)
            assert match is not None, 'Error in config INPUT-LAYOUT: ' + inp

            modality = match.group(2)
            nchannels = dinfo[modality]['n']
            path = osp.join(data_dir, dinfo[modality][match.group(1) + '-' + split])

            assert osp.exists(path), 'File not found: ' + path
            net_inps.append((inp, path, nchannels))

        for out in outs:
            # TODO: read target type: zero couplings, tight, loose couplings
            match = re.search('({})'.format('|'.join(supports)), out)
            assert match is not None, 'Error in config REFINE-TARGET: '+ out

            modality = match.group(1)
            nchannels = dinfo[modality]['n']
            path = osp.join(data_dir, dinfo[modality]['gt-' + split])

            assert osp.exists(path), 'File not found: ' + path
            net_outs.append((out, path, nchannels))

        loss_params = dict()
        mapping = None
        if 'mapping' in dinfo['seg']:
            idx = dinfo['seg']['mapping']
            mapping = dict(zip(idx, xrange(len(idx))))

        if split == 'train':

            # if the class weights is not in the dataset config file
            if 'gt-train-weights' not in dinfo['seg']:
                print 'Generating median frequency balancing weights.'
                (weights, mapping) = gcw.get_mfb(osp.join(dinfo['ROOT'], dinfo['seg']['gt-train']),
                                            dinfo['seg']['ignore_label'],
                                            mapping)
                # save back to dataset config
                dinfo['seg']['gt-train-weights'] = weights
                yaml.dump(dinfo, open(dcfg_path, 'w'), default_flow_style=False)
            else:
                weights = dinfo['seg']['gt-train-weights']
            # update data
            # update loss parameter
            ignore_label = dinfo['seg']['ignore_label']
            ignore_label = mapping[ignore_label] if mapping is not None else ignore_label
            loss_params['loss_param'] = {
                    'ignore_label': ignore_label,
                    'class_weighting': weights
                    }

        # generate net prototxt
        loader = dinfo['NAME'] + '_loader'
        net_proto = arch.create_net(net_inps, net_outs, split, loader, layout, mapping, **loss_params)

        # output to file
        path = osp.join(args.cache_dir, getattr(args, 'exp_{}_path'.format(split)))
        open(path, 'w').write(str(net_proto))
        nets[split] = net_proto

    return nets

def create_solver(args):

    kwargs = dict(
            train_net=args.exp_train_path,
            snapshot_prefix=args.snapshot_prefix
            )

    solver_proto = arch.create_solver(**kwargs)
    args.max_iter = solver_proto.max_iter
    open(args.exp_solver_path, 'w').write(str(solver_proto))


def create_cmd(nets, args):

    # load project configuration
    pinfo = yaml.load(open(args.config))

    # log option after tee
    log_path = osp.join(pinfo['OUTPUT_DIRS']['OUTPUT'], args.exp_name)
    if not osp.isdir(log_path):
        os.makedirs(log_path)
    log_option = osp.join(log_path, pinfo['NAMES']['LOG'] + args.exp_name)

    # options to train.py
    # path to solver file
    options = ' --solver ' + args.exp_solver_path
    # path to log file to plot training loss
    options += ' --log_file ' + log_option

    # path to weight/snapshot for finetuning or resuming
    if args.weight is not None:
        options += ' --weight ' + args.weight
    if args.snapshot is not None:
        options += ' --snapshot ' + args.snapsh
        # it's a resume, so better append to old logot
        log_option = ' --append ' + log_option


    # get the output blobs for on-the-fly visualization
    # read output tops from train prototxt
    blobs = []
    outblobs = []
    for l in nets['train'].layer:
        if 'Python' in l.type:
            blobs += [str(t) for t in l.top if 'img_idx' not in t]
        if 'Loss' in l.type:
            outblobs += [str(t) for t in l.bottom if t not in blobs]
    if len(blobs+outblobs) > 0:
        options += ' --blobs ' + ' '.join(blobs+outblobs)

    args.out_blobs = [b for b in outblobs if 'gt' not in b]

    # add path to the experiment dir, where the visualization are going to be saved
    options += ' --vis_path ' + args.cache_dir

    # add path to pycaffe
    options += ' --pycaffe ' + pinfo['CAFFE']


    # the full command
    cmds = list()
    cmds.append('set -x')
    cmds.append('export CUDA_VISIBLE_DEVICES={}'.format(args.gpu))
    cmds.append('python train.py {} 2>&1 | tee {}'.format(options, log_option))
    cmds.append('cp {} {}'.format(
        args.snapshot_prefix + '_iter_{:d}.caffemodel'.format(args.max_iter),
        osp.join(args.cache_dir, args.exp_name + '_testweight.caffemodel')
        ))
    cmds.append('python inference.py --config {0} --exp {1} --proto {2} '
        '--weight {3} --outdir {4} --out_blobs {5} --perimg {6} --report {7}'.format(
            args.config, # 0
            args.exp, # 1
            args.exp_test_path, #2
            args.snapshot_prefix + '_iter_{:d}.caffemodel'.format(args.max_iter), #3
            args.output_dir, #4
            ' '.join(args.out_blobs), #5
            osp.join(args.cache_dir, 'perimg.md'), #6
            osp.join(args.cache_dir, 'README.md') #7
            ))

    cmd = '\n\n'.join(cmds)
    # write command to file
    runsh = osp.join(args.cache_dir, pinfo['NAMES']['SH'])
    open(runsh, 'w').write(cmd)

    # call command to run
    print runsh
    call('chmod +x ' + runsh, shell=True)
    call(runsh, shell=True)


def process_options(args):

    # input sanitizer
    assert args.snapshot is None or args.weight is None, \
        'Either snapshot or weight can be provided, but not both.'

    # load project configuration
    pinfo = yaml.load(open(args.config))

    root = pinfo['PROJECT']['ROOT']
    args.root = root
    exp = osp.splitext(osp.basename(args.exp))[0]
    args.exp_name = exp

    # create working directory
    if args.cache_dir is None:
        args.cache_dir = osp.join(root, pinfo['PROJECT']['CACHE'], exp)
    if not osp.isdir(args.cache_dir):
        print 'Creating working directory', args.cache_dir
        os.makedirs(args.cache_dir)

    # create  model and output dirs
    args.model_dir = osp.join(pinfo['OUTPUT_DIRS']['MODEL'], exp)
    if not osp.isdir(args.model_dir):
        os.makedirs(args.model_dir)
        print 'Creating model directory', args.model_dir
    if not osp.isdir(osp.join(args.cache_dir, pinfo['NAMES']['MODEL'])):
        os.symlink(args.model_dir, osp.join(args.cache_dir, pinfo['NAMES']['MODEL']))

    args.output_dir = osp.join(pinfo['OUTPUT_DIRS']['OUTPUT'], exp)
    if not osp.isdir(args.output_dir):
        os.makedirs(args.output_dir)
        print 'Creating output directory', args.output_dir
    if not osp.isdir(osp.join(args.cache_dir, pinfo['NAMES']['OUTPUT'])):
        os.symlink(args.output_dir, osp.join(args.cache_dir, pinfo['NAMES']['OUTPUT']))

    # get paths to experiment files
    args.data_config_path = osp.join(root, pinfo['PROJECT']['CONFIG'])
    args.exp_config_path = osp.join(args.cache_dir, pinfo['NAMES']['CONFIG'])
    args.exp_train_path = osp.join(args.cache_dir, pinfo['NAMES']['TRAIN'])
    args.exp_test_path = osp.join(args.cache_dir, pinfo['NAMES']['TEST'])
    args.exp_solver_path = osp.join(args.cache_dir, pinfo['NAMES']['SOLVER'])

    snapshot_dir = args.model_dir
    if not osp.isdir(snapshot_dir):
        os.makedirs(snapshot_dir)
    args.snapshot_prefix = osp.join(snapshot_dir, exp)

    return args


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, default=None,
            help='Path to general configuration file (*.yaml)')
    parser.add_argument('--exp', required=True, default=None,
            help='Path to experiment configuration file (*.yaml)')

    # TODO: not begin used now
    parser.add_argument('--solver_template', required=False,
            help='Path to solver template to overwrite the default')
    parser.add_argument('--caffe', default='caffe',
            help='Path to python directory in caffe binary')# compiled from '
                             #'https://github.com/fyu/caffe-dilation.')
    parser.add_argument('--weight', type=str, required=False, default=None,
            help='Path to pretrained weights (*.caffemodel) to initialize the model')
    parser.add_argument('--snapshot', type=str, required=False, default=None,
            help='Path to snapshot file (*.solverstate) to resume')
    parser.add_argument('--cache_dir', default=None,
            help='Working dir for training.\nAll the generated network and '
                 'solver configurations will be written to this directory. '
                 'Training snapshots and network outputs will NOT be saved there.'
                 'cache_dir = ROOT/CACHE/EXP, by default.')
    parser.add_argument('--gpu', type=str, default='0',
            help='GPU index for training')

    # TODO: not being used now. overwritten solver parameters
    parser.add_argument('--lr', type=float, default=0,
                        help='Solver SGD learning rate to overwrite the template and default')
    parser.add_argument('--momentum', type=float, default=0.9,
                        help='Gradient momentum to overwrite the template and default')
    parser.add_argument('--iter_size', type=int, default=1,
                        help='Number of passes/batches in each iteration to overwrite the template and default.')

    args = process_options(parser.parse_args())

    nets = create_net(args)
    create_solver(args)
    create_cmd(nets, args)



if __name__ == '__main__':
    main()
