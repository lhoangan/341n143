import caffe
from input_handler import Handler as Handler

class PyDataLayer(caffe.Layer):
    def setup(self, bottom, top):
        """
        Setup data layer according to parameters:

        - nyud_dir: path to NYUDv2 dir
        - split: train / val / test
        - tops: list of tops to output from {color, depth, hha, label}
        - randomize: load in random order (default: True)
        - seed: seed for randomization (default: None / current time)

        for NYUDv2 semantic segmentation.

        example: params = dict(nyud_dir="/path/to/NYUDVOC2011", split="val",
                               tops=['color', 'hha', 'label'])
        """

        # config
        self.handler = Handler(self.param_str)
        self.tops = self.handler.get_tops()
        self.data = dict() # store top data for reshape + forward

        # data layers have no bottoms
        assert  len(bottom) == 0, \
                "The layer receive no bottoms, but is given %d" % len(bottom)
        # tops: check configuration
        assert  len(top) == len(self.tops), \
                "Require {:d} tops but receive {:d} tops in param_str " + \
                "{:d} vs. {:d}".format(len(top), len(self.tops))


    def reshape(self, bottom, top):
        # load data for tops and  reshape tops to fit (1 is the batch dim)
        for i, t in enumerate(self.tops):
            self.data[t] = self.handler.load_data(t)
            top[i].reshape(*self.data[t].shape)

    def forward(self, bottom, top):
        # assign output
        for i, t in enumerate(self.tops):
            top[i].data[...] = self.data[t]

        self.handler.next_idx()

    def backward(self, top, propagate_down, bottom):
        pass
