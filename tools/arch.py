import sys
sys.path.insert(0, '/home/hale/caffe/segflow-caffe/python')
import caffe
from caffe import layers as L
from caffe.proto import caffe_pb2

# https://stackoverflow.com/questions/32225388/lstm-module-for-caffe/35967589#35967589
# args = list of bottom blobs, kwargs for layer parameters
def make_layer(net, layer_type, name, *args, **kwargs):
    kwargs.update({'name': name})
    layer = layer_type(*args, **kwargs)
    net[name] = layer # alt: net.__setattr__(name, layer)
    return net[name] # alt: net.__getattr__(name)

# args = list of bottom blobs then list of top blobs, kwargs for layer parameters
def make_layer_multtop(net, layer_type, name, ntops, *args, **kwargs):
    kwargs.update({'name': name, 'ntop': ntops})
    num_in = len(args) - ntops #number of input blobs
    tops = layer_type(*args[:num_in], **kwargs)
    # assign to each top its name
    for i in range(ntops):
        net[args[num_in+i]] = tops[i]
    return tops

def python_param(split, inp_blobs, out_blobs, loader, mapping=None,
        batch_size=4, seed=1606, flip='0',
        module='input_layer', layer='PyDataLayer', **kwargs):


    tops = [k + '_in' for k in zip(*inp_blobs)[0]]
    tops += [k + '_gt' for k in zip(*out_blobs)[0]] + ['img_idx']
    paths = zip(*inp_blobs)[1] + zip(*out_blobs)[1]

    param_str = str(dict(
            dict(zip([t+'-path' for t in tops], paths)),
            loader=loader,
            tops=tops,
            batch_size=batch_size,
            split=split,
            seed=seed,
            flip=flip,
            mapping=mapping,
            ))
    python_param = dict(module=module, layer=layer, param_str=param_str)

    return python_param, tops

# args = list of bottom blobs, kwargs for layer parameters
def create_scale_branch(net, s, bottoms):

    nlayer_single=2 # number of layers in each single modality (before concat)
    nlayer_concat=4 # number of layers after concat
    # common parameter for each conv in each scale branch
    conv_param = dict(
            weight_filler=dict(type='msra'),
            num_output=32,
            kernel_size=3,
            stride=1,
            pad=1,
        )

    # create input branch for each modality in each scale module
    tops=[]  # list of tops, one for each modality
    # for each modality
    for input_name, bottom, nchannels in bottoms:
        # if not at original size (s > 0)
        if s > 0: # create downsampling layer
            name = '-'.join(['scale%d'%s, input_name, 'downsampling'])
            down_param = dict( # conv param for downsampling effect
                        bias_term=False,
                        param=[{'lr_mult':0, 'decay_mult': 0}],
                        weight_filler=dict(type='bilinear'),
                        num_output=nchannels,
                        group=nchannels,
                        kernel_size=1,
                        stride=2**s,
                        pad=0,
                    )
            bottom = make_layer(net, L.Convolution, name, bottom, **down_param)
        # create a sequence of conv-relu layers
        for i in range(nlayer_single):
            name = '-'.join(['scale%d'%s, input_name, 'conv%d'%i])
            bottom = make_layer(net, L.Convolution, name, bottom, **conv_param)
            name = '-'.join(['scale%d'%s, input_name, 'relu%d'%i])
            top = make_layer(net, L.ReLU, name, bottom, in_place=True)
            bottom = top # this layer's top will be next one's bottom
        tops.append(top)

    # concat layer
    name = '-'.join(['scale%d'%s, 'concat'])
    top = make_layer(net, L.Concat, name, *tops, axis=1)

    # create conv sequence after concat layer in each scale branch
    for i in range(nlayer_concat):
        name = '-'.join(['scale%d'%s, 'conv%d'%i])
        top = make_layer(net, L.Convolution, name, top, **conv_param)
        name = '-'.join(['scale%d'%s, 'relu%d'%i])
        top = make_layer(net, L.ReLU, name, top, in_place=True)

    # upsampling using Deconv layer
    # http://caffe.berkeleyvision.org/doxygen/classcaffe_1_1BilinearFiller.html
    if s > 0:
        name = '-'.join(['scale%d'%s, 'upsampling'])
        up_param = dict( # conv param for downsampling effect
                    bias_term=False,
                    weight_filler=dict(type='bilinear'),
                    num_output=32, # the same as output of bottom (conv layer)
                    group=32,
                    kernel_size=2*2**s, # generally, 2*factor - factor%2
                    stride=2**s,
                    pad=2**s/2, # generally, ceil((factor-1)/2.)
                )
        top = make_layer(net, L.Deconvolution, name, top,
                convolution_param=up_param,
                param=[{'lr_mult':0, 'decay_mult': 0}])

    return top

# layout = ['prseg, prflow', 'gtnorm'] # list of strings
def create_input_concat(net, bottoms, layout):

    # each l become 1 meta-input branch
    tops = []
    for l in layout:
        ns = [s.strip() for s in l.split(',')] # names
        comb = [(b[1], b[2]) for b in bottoms if len([n for n in ns if n in b[0]]) > 0]
        bots, nchans = zip(*comb)
        if len(ns) > 1:
            top = make_layer(net, L.Concat, '-'.join(ns), *bots, axis=1)
        else:
            top = bots[0]
        tops.append(('-'.join(ns), top, sum(nchans)))

    return tops

# bottoms and tops: dict of type {'modality': nchannel/top}
# when len(bottoms) == 1, bottoms is list [bottom]
# returned tops in tops[i][1]
def create_output_layers(net, tops, **conv_param):

    # each top is of format: {'modality': [top, nchannel]}
    out_tops = []
    for out_type, top, nchannels in tops:
        name = '-'.join(['out', out_type])
        # remake the same tuple with updated new tops
        top = make_layer(net, L.Convolution, name, top, num_output=nchannels, **conv_param)
        out_tops.append((out_type, top, nchannels))
        if out_type == 'seg':
            bottom = make_layer(net, L.Softmax, 'prob', top)
            make_layer(net, L.Silence, 'silence', bottom, ntop=0) # Silence layer requires no top
    return out_tops

def create_loss_layers(net, tops, gt_tops, **loss_params):

    out_tops = []
    for out_type, top, nchannels in tops:
        name = '-'.join(['loss', out_type])
        if out_type == 'norm' or out_type == 'flow':
            loss_type = L.L1Loss
            kwargs = dict(l2_per_location=True, normalize_by_num_entries=True)
        elif out_type == 'seg':
            kwargs = loss_params
            make_layer(net, L.Accuracy, 'accuracy', top, gt_tops[out_type],
                    top='per_class_accuracy', ignore_label=kwargs['loss_param']['ignore_label'])
            loss_type = L.SoftmaxWithLoss
        else:
            raise Exception('Unknown out_type modality' + out_type)
        top = make_layer(net, loss_type, name, top, gt_tops[out_type], **kwargs)
        out_tops.append((out_type, top, nchannels))
    return out_tops


# inp = [('modality', input_file, nchannels), ...]
# out = [('modality', label_file, nchannels), ...]
# not working for deploy case (inference without ground truth label)
def create_net(inps, outs, split, loader, layout, mapping=None, couplings='zero', **loss_param):
    net = caffe.NetSpec()

    # Input layer
    inp, ipaths, ichans = zip(*inps)
    out, opaths, ochans = zip(*outs)
    batch_size = 4 if split=='train' else 1
    input_params, top_names = python_param(split, zip(inp, ipaths), zip(out, opaths),
            loader, mapping, batch_size=batch_size)
    tops = make_layer_multtop(net, L.Python, 'Input', len(top_names), *top_names, **input_params)

    ninp = len(inp)
    bottoms = zip(top_names[:ninp], tops[:ninp], ichans)
    # TODO create meta input to scale branches (merge few input together if required)
    bottoms = create_input_concat(net, bottoms, layout)

    # create scale branches
    scale_tops = []
    for i in range(4): # 4 scale branches
        top = create_scale_branch(net, i, bottoms)
        scale_tops.append(top)


    # concat all scale branches
    top = make_layer(net, L.Concat, 'main-concat', *scale_tops, axis=1)

    # squence of conv-relu layers after concat
    nouts = [128, 64, 32] # num_outputs
    conv_param = dict(
            weight_filler=dict(type='msra'),
            kernel_size=3,
            stride=1,
            pad=1,
        )
    for i in range(len(nouts)):
        name = '-'.join(['main', 'conv%d'%i])
        top = make_layer(net, L.Convolution, name, top, num_output=nouts[i], **conv_param)
        name = '-'.join(['main', 'relu%d'%i])
        top = make_layer(net, L.ReLU, name, top, in_place=True)

    # create output layers, convention, list of [top, nchannel]
    net_outs = list(zip(out, [top]*len(out), ochans))
    net_outs = create_output_layers(net, net_outs, **conv_param)

    # create loss layer for training
    if split == 'train':
        create_loss_layers(net, net_outs, dict(zip(out, tops[ninp:ninp+len(out)])), **loss_param)

    return net.to_proto()

def create_solver(**kwargs):
    solver = caffe_pb2.SolverParameter(**kwargs)

    #solver.train_net = train_net
    #if 'test_net' in kwargs:
    #    solver.test_net.append(kwargs[)
    #    solver.test_iter.append(50)
    #    solver.test_interval = 100

    solver.base_lr = 1e-4 #options.lr
    solver.lr_policy = "step"
    solver.gamma = 0.5
    solver.stepsize = 50000
    solver.momentum = 0.9 #options.momentum

    # regularization 
    # https://stackoverflow.com/questions/32177764/what-is-weight-decay-meta-parameter-in-caffe
    solver.weight_decay = 0.0005
    #solver.regularization_type = 'L2'

    solver.display = 100
    solver.snapshot = 50000
    solver.max_iter = 200000
    solver.solver_mode = solver.GPU
    #solver.iter_size = options.iter_size
    #solver.snapshot_format = solver.BINARYPROTO
    #solver.type = 'SGD'
    #solver.snapshot_prefix = options.snapshot_prefix

    return solver


