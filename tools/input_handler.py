import random

class Handler(object):
    def __init__(self, param_str):

        params = eval(param_str)

        # create loader
        assert 'loader' in params, \
                'Dataset loader not found. Specify it with \'loader\' in param_str'
        loader = None
        exec('from {0} import {0} as loader'.format(params['loader']))
        self.loader = loader(params, self)

        # load indices for images and labels
        self.tops = params['tops']
        self.input_tops(params)

        self.split = params['split']
        self.batch_size = params.get('batch_size', 1)
        self.random = params.get('randomize', True)
        self.seed = params.get('seed', None)
        self.cropped_size = None # TODO: params.get('cropped_size', None) # (height, width)
        self.mappings = params.get('mappings', None)
        self.niters = params.get('niters', self.inlen)

        assert  self.niters <= self.inlen, \
                "Number of iterations must less than or equal to number of " + \
                "data point but {:d} vs. {:d}".format(self.niters, self.inlen)

        # make evaluation deterministic
        if 'train' not in self.split:
            self.random = False
            if self.niters == self.inlen:
                self.indices = range(self.inlen)
            else:
                # if we would only run a small number of iteration
                # it is better to shuffle (but deterministically) the dataset
                # to have a good variation during test or validation
                random.seed(1) # fixed seed
                self.indices = random.sample(range(self.inlen), self.inlen)
            self.do_flip = int(params.get('flip', 0))
        else:
            random.seed(self.seed)
            self.indices = random.sample(range(self.inlen), self.inlen)
            self.do_flip = int(params.get('flip', 1))

        # preparing crop
        if self.cropped_size is not None:
            assert  len(self.cropped_size) == 2, \
                    'cropped_size must be a 2-tuple of (height, width), ' + \
                    'but receive {:s}'.format(str(self.cropped_size))
            self.cropped_start_y = None
            self.cropped_start_x = None

        # initialization
        self.epoch = 1
        self.idx = 0
        self.next_idx()

    def get_tops(self):
        return self.tops

    def input_tops(self, params):
        self.inlen = None # len of input lists, size of dataset
        self.refer_top = None
        for top in self.tops:
            if top == 'img_idx':
                continue
            exec("self.{0:} = open(params['{0:}-path']).read().splitlines()".format(top))
            if self.inlen is None:
                self.inlen = eval('len(self.{})'.format(top))
                self.refer_top = top
            else:
                inlen = eval('len(self.{})'.format(top))
                assert inlen == self.inlen, \
                    "Input lists are of different length: {} has {:d}".format(
                    top, inlen) + "files, while {} has {:d} files".format(
                    self.refer_top, self.inlen)

    def next_idx(self):
        # pick next input
        if self.idx + self.batch_size > self.niters:
            self.epoch += 1
            self.idx = 0
            if self.random:
                # random.seed(self.seed)
                self.indices = random.sample(range(self.inlen), self.inlen)
        self.batch_idx = range(self.idx, self.idx + self.batch_size)
        self.idx += self.batch_size

        # flip_idx == 1 means NO flip (do_flip == 0), otherwise flip_idx == -1
        self.flip_idx = int((0.5-(self.epoch % 2))*2) # flip at odd epoch
        # overwrite flip_idx with self.do_flip (0 = no flip, 1 = allow flip)
        self.flip_idx = self.flip_idx * self.do_flip + (1 - self.do_flip)


    def load_data(self, top):
        """ Load given bottom data"""
        assert 'load_{}'.format(top) in dir(self.loader), \
                "No handle function defined for top name: {}".format(top)
        return eval('self.loader.load_{}()'.format(top))
