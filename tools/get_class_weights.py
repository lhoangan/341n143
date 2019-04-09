import numpy as np
from PIL import Image



# argv[1] : annotation path files 
# argv[2] : number of expected (real) classes, without void/unknown class
# argv[3] : label mapping, used if input is raw mat file


# compute median frequency balancing
# D. Eigen and R. Fergus, "Predicting depth, surface normals and semantic
# labels with a common multi-scale convolutional architecture," in ICCV,
# pp. 2650-2658, 2015
def get_mfb(pathlist_file, void_label=None, mapping=None):

    # anno_paths: list of path to annotation images
    # mapping: dict(idx: new_idx) map the labels to range [0..len(labels)]
    # void_label: void label in raw label set (before being mappped)

    anno_paths = open(pathlist_file).read().splitlines()

    counts = dict()
    allpix = dict()
    weights = dict()
    for path in anno_paths:
        anno = np.array(Image.open(path))
        labels, count = np.unique(anno, return_counts=True)
        npixels = np.product(anno.shape[:2])
        for l,c in zip(labels, count):
            counts[l] = counts.get(l, 0) + c
            allpix[l] = allpix.get(l, 0) + npixels

    # compute frequency
    for k in counts:
        weights[k] = float(counts[k]) / float(allpix[k])
    med = np.median(weights.values())
    # compute median frequency balance
    for k in counts:
        weights[k] = med / weights[k]

    # if no mapping given, get the mapping by the keys' order
    if mapping is None:
        mapping = dict(zip(sorted(weights.keys()), np.arange(len(weights.keys()))))
    # if no void_label given, pop the largest key
    if void_label is None:
        void_label = max(weights.keys())
    # delete void_label
    weights.pop(void_label, None)

    # map the keys
    mfbs = dict()
    for k in weights:
        mfbs[mapping[k]] = weights[k]

    # sorted (according to newly mapped labels
    (keys, values) = zip(*sorted(mfbs.items()))

    return [float(v) for v in values], mapping



