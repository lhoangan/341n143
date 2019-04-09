import re
import numpy as np
from PIL import Image
from input_utils import Input_Utils
import scipy.io as sio

class gdxtracted_loader(Input_Utils):

    def __init__(self, params, handler):
        Input_Utils.__init__(self, params, handler)

        # number of classes for segmentation for vkitti dataset
        self.nclasses = 15

        # mapping
        if 'mapping' in params:
            self.mapping = params['mapping']

        # supported modalities
        modalities = ['seg', 'flow', 'norm', 'depth']
        types = ['gt', 'pr']

        # read path lists into class attributes, such as self.prflow, self.gtseg, etc.
        for k in params:
            m = re.search('({})'.format('|'.join(modalities)), k)
            t = re.search('({})'.format('|'.join(types)), k)
            if m and t:
                attr = t.group(1)+m.group(1)
                # read path list into 
                paths = open(params[k]).read().splitlines()
                # save the paths into class attributes, e.g. self.prflow, self.gtseg
                setattr(self, attr, paths)

    def load_flow(self, paths):

        out = None
        for i in self.batch_idx:
            flow  = self.flow_read(paths[self.indices(i)]).astype(np.float32)

            # flip horizontally
            flow = flow[:, ::self.flip_idx, ...]
            flow[np.isnan(flow)] = 0
            flow = flow[:,:,::-1]
            flow = flow.transpose((2,0,1))
            flow = flow[np.newaxis, ...]
            out = flow if out is None else np.concatenate((out, flow))
        return out

    def load_prflow_in(self):
        return self.load_flow(self.prflow)

    def load_gtflow_in(self):
        return self.load_flow(self.gtflow)

    def load_flow_gt(self):
        return self.load_flow(self.gtflow)


    def load_segim(self, paths):
        """
        Load segmentation annotaion as ground truth label
        Input: paths to 1-channel image (usually indexed png),
            whose pixels indicate object classes (0 to n classes)
        Output: tensor of n x 1-channel images
        """
        out = None
        for i in self.batch_idx:
            segim = np.array(Image.open(paths[self.indices(i)]), dtype=np.int16)
            segim = self.map_im(segim, self.mapping)

            segim = segim[:, ::self.flip_idx, ...]
            segim = segim[None, None, ...]
            out = segim if out is None else np.concatenate((out, segim))
        return out


    def load_segscore(self, paths):
        """
        Load segmentation score from file
        Input: paths to m-channel mat files (probability softmax score)
        Output: tensor of n x m-channel images
        """
        out = None
        for i in self.batch_idx:
            segscore = sio.loadmat(paths[self.indices(i)])['score'].astype(np.float32)

            segscore = segscore.transpose((1, 2, 0))[:, ::self.flip_idx, ...]
            segscore[np.isnan(segscore)] = 0
            segscore = segscore.transpose((2,0,1))
            segscore = segscore[None, ...]
            out = segscore if out is None else np.concatenate((out, segscore))
        return out

    def load_segim2score(self, paths):
        """
        Load segmentation annotaion as ground truth label
        Input: paths to 1-channel image (usually indexed png),
            whose pixels indicate object classes (0 to n classes)
        Output: tensor of n x 1-channel images
        """
        out = None
        for i in self.batch_idx:
            segim = np.array(Image.open(paths[self.indices(i)]), dtype=np.int16)
            segim = self.map_im(segim, self.mapping)

            segscore = self.anno_to_hard_onehot(segim, self.nclasses)

            segscore = segscore[:, ::self.flip_idx, ...]
            segscore = segscore.transpose((2,0,1))
            segscore = segscore[None, ...]
            out = segscore if out is None else np.concatenate((out, segscore))
        return out

    def load_prseg_in(self):
        return self.load_segscore(self.prseg)

    def load_gtseg_in(self):
        return self.load_segim2score(self.gtseg)

    def load_seg_gt(self):
        return self.load_segim(self.gtseg)

    def load_prnorm(self, paths):

        out = None
        for i in self.batch_idx:
            norm   = sio.loadmat(paths[self.indices(i)])['predns'].astype(np.float32)

            norm = norm.astype(np.float32)
            norm = norm[:, ::self.flip_idx, ...] # flip horizontally
            norm[np.isnan(norm)] = 0
            norm = norm[:,:,::-1]
            norm = norm.transpose((2,0,1))
            norm = norm[np.newaxis, ...]
            out = norm if out is None else np.concatenate((out, norm))
        return out

    def load_gtnorm(self, paths):

        out = None
        for i in self.batch_idx:
            norm = sio.loadmat(paths[self.indices(i)])['normal'].astype(np.float32)

            norm = norm[:, ::self.flip_idx, ...]
            norm[np.isnan(norm)] = 0
            norm = norm.transpose((2,0,1))
            norm = norm[np.newaxis, ...]
            out = norm if out is None else np.concatenate((out, norm))
        return out

    def load_prnorm_in(self):
        return self.load_prnorm(self.prnorm)

    def load_gtnorm_in(self):
        return self.load_gtnorm(self.gtnorm)

    def load_norm_gt(self):
        return self.load_gtnorm(self.gtnorm)

    def load_gtdepth(self, paths):

        out = None
        for i in self.batch_idx:
            depth = sio.loadmat(paths[self.indices(i)])['depth'].astype(np.float32)

            depth = depth[:, ::self.flip_idx, ...]
            depth[np.isnan(depth)] = 0
            depth = depth[None, None, ...]
            out = depth if out is None else np.concatenate((out, depth))
        return out

    def load_gtdepth_in(self):
        return self.load_gtdepth(self.gtdepth)

    def load_depth(self):
        return self.load_gtdepth(self.gtdepth)

