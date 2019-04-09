import re
import os, os.path as osp
import net
import yaml
import argparse

import get_class_weights as gcw

infos = {
        'vkitti': {
            'rgb': {
                'n': 3,
                'gt-train': 'vkitti/rgb.train',
                'gt-test': 'vkitti/rgb.test',
            },
            'seg': {
                'n': 13,
                'gt-train': 'vkitti/anno.train',
                'gt-test': 'vkitti/anno.test',
                'pr-train': 'vkitti/resnet_score.train',
                'pr-test': 'vkitti/resnet_score.test'
            },
            'flow': {
                'n': 2,
                'gt-train': 'vkitti/flow.train',
                'gt-test': 'vkitti/flow.test',
                'pr-train': 'vkitti/flownetc.train',
                'pr-test': 'vkitti/flownetc.test'
            },
            'norm': {
                'n': 3,
                'gt-train': 'vkitti/normal.train',
                'gt-test': 'vkitti/normal.test',
                'pr-train': 'vkitti/pred_normal.train',
                'pr-test': 'vkitti/pred_normal.test'
            },
        'gdxtracted': {
            'rgb': {
                'n': 3,
                'gt-train': 'gdxtracted/rgb.train',
                'gt-test': 'gdxtracted/rgb.test',
            },
            'seg': {
                'n': 15,
                'gt-train': 'gdxtracted/anno.train',
                'gt-test': 'gdxtracted/anno.test',
                'pr-train': 'gdxtracted/segnet_score.train',
                'pr-test': 'gdxtracted/segnet_score.test'
            },
            'flow': {
                'n': 2,
                'gt-train': 'gdxtracted/flow.train',
                'gt-test': 'gdxtracted/flow.test',
                'pr-train': 'gdxtracted/flownetc.train',
                'pr-test': 'gdxtracted/flownetc.test'
            },
            'norm': {
                'n': 3,
                'gt-train': 'gdxtracted/fnormals.train',
                'gt-test': 'gdxtracted/fnormals.test',
                'pr-train': 'gdxtracted/pred_normals.train',
                'pr-test': 'gdxtracted/pred_normals.test'
            },
        }
    }
}

parser = argparse.ArgumentParser()
parser.add_argument('--cache_dir', type=str, default='runs')
parser.add_argument('--config', type=str, required=True)
args = parser.parse_args()

root = '/home/hale/TrimBot/projects/341n143'
exp = osp.splitext(osp.basename(args.config))[0]
data_dir = osp.join(root, 'data')
runs_dir = osp.join(root, args.cache_dir, exp)


# Load config file
cfg = yaml.load(open(args.config))

# copy config to run directory
if not osp.isdir(runs_dir):
    os.makedirs(runs_dir)
# output config file
yaml.dump(cfg, open(osp.join(runs_dir, 'config.yaml'), 'w'), default_flow_style=False)

dcfg_path = osp.join(root, 'configs', cfg['INPUT']['DATASET'])
dinfo = yaml.load(open(dcfg_path))

dataset = dinfo['NAME']
inps = [s.strip() for s in cfg['INPUT']['LAYOUT'].split(',')]
outs = [s.strip() for s in cfg['REFINE']['TARGETS'].split(',')]

supports = ['seg', 'flow', 'norm', 'rgb']

for split in ['train', 'test']:
    net_inps = []
    net_outs = []
    for inp in inps:
        match = re.search('^(gt|pr)({})'.format('|'.join(supports)), inp)
        assert match is not None, 'Error in config INPUT-LAYOUT: ' + inp

        modality = match.group(2)
        nchannels = infos[dataset][modality]['n']
        path = osp.join(data_dir, infos[dataset][modality][match.group(1) + '-' + split])

        assert osp.exists(path), 'File not found: ' + path
        net_inps.append((inp, path, nchannels))

    for out in outs:
        # TODO: read target type: zero couplings, tight, loose couplings
        match = re.search('({})'.format('|'.join(supports)), out)
        assert match is not None, 'Error in config REFINE-TARGET: '+ out

        modality = match.group(1)
        nchannels = infos[dataset][modality]['n']
        path = osp.join(data_dir, infos[dataset][modality]['gt-' + split])

        assert osp.exists(path), 'File not found: ' + path
        net_outs.append((out, path, nchannels))


    mapping = None
    if 'mapping' in dinfo['seg']:
        idx = dinfo['seg']['mapping']
        mapping = dict(zip(idx, xrange(len(idx))))

    loss_params = dict()
    if split == 'train':

        # if the class weights is not in the dataset config file
        if 'gt-train-weights' not in dinfo['seg']:
            print 'Generating median frequency balancing weights.'
            (weights, _) = gcw.get_mfb(osp.join(dinfo['ROOT'], dinfo['seg']['gt-train']),
                                        dinfo['seg']['ignore_label'],
                                        mapping)
            # save back to dataset config
            #weights = [float(w) for w in weights]
            dinfo['seg']['gt-train-weights'] = weights
            yaml.dump(dinfo, open(dcfg_path, 'w'), default_flow_style=False)
        else:
            weights = dinfo['seg']['gt-train-weights']
        # update data
        # update loss parameter
        loss_params['loss_param'] = {
                'ignore_label': dinfo['seg']['ignore_label'],
                'class_weighting': weights
        }

    # generate net prototxt
    loader = dataset + '_loader'
    net_proto = net.create_net(net_inps, net_outs, split, loader, **loss_params)

    # output to file
    open(osp.join(runs_dir, split + '.pt'), 'w').write(str(net_proto))

