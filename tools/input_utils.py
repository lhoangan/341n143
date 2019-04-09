import numpy as np
import random as rn


# TODO: experimental
class Input_Utils(object):

    def __init__(self, params, handler):
        self.params = params
        self.handler = handler

    def indices(self, i):
        return self.handler.indices[i]

    @property
    def flip_idx(self):
        return self.handler.flip_idx

    @property
    def batch_idx(self):
        return self.handler.batch_idx

    # output image index
    def load_img_idx(self):
        return np.array([self.indices(i) for i in self.batch_idx])

    def map_im(self, lhs, mapping):
        # unknown label to be the largest value
        unknown_label = max(mapping.values())
        rhs = np.zeros(lhs.shape[:2], dtype=np.uint8) + unknown_label
        for k in mapping:
            rhs[lhs == k] = mapping[k]
        return rhs

    def anno_to_hard_onehot(self, anno, nchannels):
        """
        Input:
            anno: 1-channel segmentation annotation image with normalized label values:
                the label values must belong to the continuous range [0..k], k = max label
        Output:
            segment: n-channels one-hot encoding of the annotation
        """
        segment = np.zeros(anno.shape + (nchannels,))
        for i in range(nchannels):
            segment[..., i] = (anno == i).astype(np.uint8)

        return segment

    # TODO
    def anno_to_solf_onehot(self):
        pass


    # TODO: not implemented yet
    def crop(self, img):
        return img

    # TODO: experimental
    def get_crop_cont(self, im_shape):
        sx = sy = 0
        ey = im_shape[0]
        ex = im_shape[1]
        if self.cropped_size is not None:
            assert self.cropped_size[0] <= im_shape[0], 'cropped height must <= current height '
            assert self.cropped_size[1] <= im_shape[1], 'cropped width must <= current width '

            if self.cropped_start_y is None and self.cropped_start_x is None:
                self.cropped_start_y = rn.randint(0, im_shape[0] - self.cropped_size[0])
                self.cropped_start_x = rn.randint(0, im_shape[1] - self.cropped_size[1])

            sy = self.cropped_start_y
            sx = self.cropped_start_x
            ey = sy + self.cropped_size[0]
            ex = sx + self.cropped_size[1]

            assert ey < im_shape[0], 'crop end index larger than image height'
            assert ex < im_shape[1], 'crop end index larger than image width'

        return  (range(sx, ex), range(sy, ey))


    # TODO: experimental
    def get_crop_idx(self,org_size,tar_size):
        '''get the indices of rows/columns to be removed when sub-sample an image
        org_size: original number of either rows or columns, say 1024
        tar_size: target number of either rows or columns, say 480'''

        if org_size <= 2 * tar_size:
            l = (org_size - tar_size) / 2
            return range(l, l+tar_size )

        step = org_size / tar_size
        rem = org_size % tar_size
        if rem == 0:
            return range(step/2, org_size, step)

        # the idea is that we divide the original size by the target size to get the 
        # step or stride between 2 rows/columns in the oringal image that will go into 
        # the new image. Yet, we don't want to leave so much of the original image
        # when the division is not complete. Say, 2048 / 480 will leave the last 
        # 128 pixels of the original image. To resolve this, I suggest distributing
        # that 128 pixels to both beginning and end of the original image in terms of
        # making the stride for the first and last 64 intervals become 5 (instead of 4)

        l = rem / 2 + 1 # count the number of intervals from the start, 65 in case of 2048 and 480
        r = rem - l
        x = range(step, (step+1) * l, step+1) # the index for the first l interval (step + 1)
        x = x + range(x[-1] + step-1, x[-1] + step * (tar_size - rem), step) # step
        x = x + range(x[-1] + (step+1) - 1, x[-1] + (step+1) * r, step+1) # step + 1

        if len(x) != tar_size:
            print 'Warning index length mismatch', org_size, tar_size
            return None
        if max(x) >= org_size:
            print 'Warning index exceed max values', org_size, tar_size
            return None

        return x


    # TODO: experimental
    # for simplicity, we don't use cropped size for now
    # just crop half an image
    def crop_for_test(self, im):
        nw = 4
        nh = 4
        h2 = im.shape[0] / nh
        w2 = im.shape[1] / nw
        output = None
        # FORTRANS order
        for j in range(nw):
            for i in range(nh):
                cropped = im[i*h2:(i+1)*h2, j*w2:(j+1)*w2, ...]
                cropped = cropped[None, ...]
                if output is None:
                    output = cropped
                else:
                    output = np.concatenate((output, cropped), axis=0)

        return output

    def flow_read(self, filename):
        """ Read optical flow from file, return (U,V) tuple.
        Original code by Deqing Sun, adapted from Daniel Scharstein.
        """
        TAG_FLOAT = 202021.25

        f = open(filename,'rb')
        check = np.fromfile(f,dtype=np.float32,count=1)[0]
        assert check == TAG_FLOAT, \
                ' flow_read:: Wrong tag in flow file ' +\
                '(should be: {0}, is: {1}). Big-endian machine?'.format(TAG_FLOAT,check) +\
                ' | Filename: {}'.format(filename)
        width = np.fromfile(f,dtype=np.int32,count=1)[0]
        height = np.fromfile(f,dtype=np.int32,count=1)[0]
        size = width*height
        assert width > 0 and height > 0 and size > 1 and size < 100000000, \
            ' flow_read:: Wrong input size (width = {0}, height = {1}).'.format(width,height)

        tmp = np.fromfile(f,dtype=np.float32,count=-1).reshape((height,width*2))
        u = tmp[:,np.arange(width)*2]
        v = tmp[:,np.arange(width)*2 + 1]
        return np.dstack((u,v))

    def flow_write(self, filename,uv,v=None):
        """ Write optical flow to file.
        If v is None, uv is assumed to contain both u and v channels,
        stacked in depth.

        Original code by Deqing Sun, adapted from Daniel Scharstein.
        """
        TAG_CHAR = 'PIEH'
        nBands = 2

        if v is None:
            assert(uv.ndim == 3)
            assert(uv.shape[2] == 2)
            u = uv[:,:,0]
            v = uv[:,:,1]
        else:
            u = uv

        assert(u.shape == v.shape)
        height,width = u.shape
        f = open(filename,'wb')
        # write the header
        f.write(TAG_CHAR)
        np.array(width).astype(np.int32).tofile(f)
        np.array(height).astype(np.int32).tofile(f)
        # arrange into matrix form
        tmp = np.zeros((height, width*nBands))
        tmp[:,np.arange(width)*2] = u
        tmp[:,np.arange(width)*2 + 1] = v
        tmp.astype(np.float32).tofile(f)
        f.close()


