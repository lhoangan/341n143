import matplotlib
matplotlib.use('agg') # prevent showing plot, just to save plot to file

import sys
import os.path as osp
import matplotlib.pyplot as plt
import scipy.misc as smc

import flow

from plot_log import plot_log, parse_log

import argparse

# solver parameter
parser = argparse.ArgumentParser()
parser.add_argument('--solver', type=str, required=True,
        help='Path to solver file: loaded if exists otherwise generated using default params')
parser.add_argument('--gpu', type=int, required=False, default=0,
        help='GPU number to be used')
parser.add_argument('--max_iter', type=int, required=False, default=None,
        help='Number of iterations to overwrite solver')

# training tools
parser.add_argument('--pycaffe', type=str, required=False, default=None,
        help='Path to caffe/python')
parser.add_argument('--weight', type=str, required=False, default=None,
        help='Path to pretrained weights (*.caffemodel) to finetune')
parser.add_argument('--snapshot', type=str, required=False, default=None,
        help='Path to snapshot file (*.solverstate) to resume')
parser.add_argument('--log_file', type=str, required=False, default=None,
        help='Path to log file')
parser.add_argument('--vis_path', type=str, required=False, default=None,
        help='Path to visualization folder')
parser.add_argument('--blobs', nargs='+', required=False, default=None,
        help='Blobs to be visualized')
parser.add_argument('--plot', type=str, required=False, default='train',
        help='Name for the training loss plot')

args = parser.parse_args()

# input sanitizer
assert args.snapshot is None or args.weight is None, \
    'Either snapshot or weight can be provided, but not both.'

# ============================================================================= 

# path to caffe python
if args.pycaffe is not None:
    sys.path.insert(0, args.pycaffe)

# load caffe
import caffe
from caffe.proto import caffe_pb2
from google.protobuf import text_format

caffe.set_mode_gpu()
caffe.set_device(args.gpu)

solver = caffe.get_solver(args.solver)
if args.snapshot is not None:
    solver.restore(args.snapshot)
if args.weight is not None:
    solver.net.copy_from(args.weight)

# use max_iter as provided or read from solver
max_iter = args.max_iter
if max_iter is None:
    # parse solver file and pick the max_iter field
    # https://stackoverflow.com/questions/31823898/changing-the-solver-parameters-in-caffe-through-pycaffe
    solver_config = caffe_pb2.SolverParameter()
    with open(args.solver) as f:
            text_format.Merge(str(f.read()), solver_config)
    max_iter = solver_config.max_iter

# ------------------------------------------
# do network surgery
# solver.net.copy_from(weight1)
# solver.net.copy_from(weight2)
# other surgery


# ------------------------------------------
# start training
net = solver.net

while solver.iter < max_iter:
    solver.step(1)

    if solver.iter % 100 == 0 and args.vis_path is not None:
        if args.log_file is not None and solver.iter > 200:
            plot_log(path=osp.join(args.vis_path, args.plot+".png"), **parse_log(args.log_file))
        if args.blobs is not None:
            blobs = args.blobs
            batch_size = net.blobs[blobs[0]].data.shape[0]
        else:
            continue
        for j in range(batch_size):
            for b in blobs:
                if 'seg' in b:
                    if 'gt' in b:
                        anno = net.blobs[b].data[j, 0, ...]
                    else:
                        anno = net.blobs[b].data[j, ...].argmax(axis=0)
                    cmap = plt.cm.Paired # use a simple color map
                    norm = plt.Normalize(vmin=0, vmax=40) #anno.max())
                    im = cmap(norm(anno))
                elif 'flow' in b:
                    im = flow.to_color(net.blobs[b].data[j, ::-1, ...].transpose((1, 2, 0)))
                elif 'norm' in b:
                    im = net.blobs[b].data[j, ::-1, ...].transpose((1, 2, 0))
                elif 'depth' in b:
                    depth = net.blobs[b].data[j, 0, ...]
                    cmap = plt.cm.jet # use a simple color map
                    norm = plt.Normalize(vmin=0, vmax=200) #anno.max())
                    im = cmap(norm(depth))
                smc.imsave(osp.join(args.vis_path, 'vis%d_'%j + b + '.png'), im)

