import numpy as np
from math import pi

def to_color(flow):
    UNKNOWN_FLOW_THRESH = 1e9

    h, w, nBands = flow.shape

    assert nBands == 2, 'flow_to_color: image must have two bands'

    u = flow[:, :, 0]
    v = flow[:, :, 1]

    maxu = -999
    maxv = -999

    minu = 999
    minv = 999

    maxrad = -1

    # fix unknown flow
    idxUnknown = (np.abs(u) > UNKNOWN_FLOW_THRESH) | (np.abs(v) > UNKNOWN_FLOW_THRESH)
    u[idxUnknown] = 0
    v[idxUnknown] = 0

    maxu = max(maxu, np.max(u))
    maxv = max(maxv, np.max(v))
    minu = min(minu, np.min(u))
    minv = min(minv, np.min(v))

    rad = np.sqrt(np.square(u) + np.square(v))
    maxrad = max(maxrad, np.max(rad))

    #print ('max flow: %f

    u = u/(maxrad + np.finfo(np.float).eps)
    v = v/(maxrad + np.finfo(np.float).eps)

    # compute color
    img = compute_color(u, v)

    # unknown flow
    IDX = np.tile(idxUnknown[..., None], [1, 1, 3])
    img[IDX] = 0

    return img



def compute_color(u, v):

    nanIdx = np.isnan(u) | np.isnan(v)
    u[nanIdx] = 0
    v[nanIdx] = 0

    img = np.zeros(list(u.shape)+ [3], dtype=np.uint8)

    color_wheel = make_color_wheel()
    ncols = color_wheel.shape[0]

    rad = np.sqrt(np.square(u) + np.square(v))

    a = np.arctan2(-v, -u) / pi

    fk = (a + 1) / 2 * (ncols - 1) # (-1):1 mapped to 0:ncols

    k0 = np.floor(fk).astype(np.int32)

    k1 = k0 + 1
    k1[k1 == ncols] = 1

    f = fk - k0

    for i in range(color_wheel.shape[1]):
        tmp = color_wheel[:, i]
        col0 = tmp[k0] / 255
        col1 = tmp[k1] / 255
        col = (1 - f) * col0 + f * col1

        idx = rad <= 1  # boolean type
        col[idx] = 1 - rad[idx] * (1 - col[idx])    # increase saturation with radius
        col[~idx] = col[~idx] * .75           # out of range

        img[:, :, i] = np.floor(255 * col * (1 - nanIdx)).astype(np.uint8)

    return img

# color enconding scheme
# followed the Sintel implementation of
# the color circle idea described at
# http://members.shaw.ca/quadibloc/other/colint.htm
def make_color_wheel():
    RY = 15
    YG = 6
    GC = 4
    CB = 11
    BM = 13
    MR = 6

    ncols = RY + YG + GC + CB + BM + MR
    color_wheel = np.zeros((ncols, 3)); # r, g, b

    col = 0
    # RY
    color_wheel[np.arange(RY), 0] = 255;
    color_wheel[np.arange(RY), 1] = np.floor(255 * np.arange(RY) / RY)
    col += RY

    # YG
    color_wheel[col + np.arange(YG), 0] = 255 - np.floor(255 * np.arange(YG) / YG)
    color_wheel[col + np.arange(YG), 1] = 255
    col += YG

    # GC
    color_wheel[col + np.arange(GC), 1] = 255
    color_wheel[col + np.arange(GC), 2] = np.floor(255 * np.arange(GC) / GC)
    col += GC

    # CB
    color_wheel[col + np.arange(CB), 1] = 255 - np.floor(255 * np.arange(CB) / CB)
    color_wheel[col + np.arange(CB), 2] = 255
    col += CB

    # BM
    color_wheel[col + np.arange(BM), 2] = 255
    color_wheel[col + np.arange(BM), 0] = np.floor(255 * np.arange(BM) / BM)
    col += BM

    # MR
    color_wheel[col + np.arange(MR), 2] = 255 - np.floor(255 * np.arange(MR) / MR)
    color_wheel[col + np.arange(MR), 0] = 255

    return color_wheel




def flow_read(filename):
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

def flow_write(filename,uv,v=None):
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


