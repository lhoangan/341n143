# 341n143
Source code for the paper "Three for one and one for three: Flow, Segmentation, and Surface Normals" (BMVC 2018)

If you find the repository useful, please consider citing the paper 

```
@inproceedings{le18bmvc,
 author = {Hoang-An Le and Anil Baslamisli and Thomas Mensink and Theo Gevers},
 title = {Three for one and one for three: Flow, Segmentation, and Surface Normals},
 booktitle = {British Machine Vision Conference (BMVC)},
 year = {2018},
}
```

## Data

Parts of the Virtual KITTI dataset are included in this repository for your convenience.
If used, please cite the corresponding paper following the instructions at
[NAVER LABS EUROPE](http://www.europe.naverlabs.com/Research/Computer-Vision/Proxy-Virtual-Worlds)

Ground truth surface normals are converted from the provided depth images using
the method given by [Barron and Malik, Shape, Illumination, and Reflectance from
Shading](https://drive.google.com/file/d/1vg9Rb-kBntSTnTCzVgFlskkPXvTB_5aq/view).
The source code is available in the [project page](https://jonbarron.info/) or 
[here](). Please cite the according paper if you use the codes in your research.


- Virtual KITTI
  - Optical flow:
    [ground truth (7 GB)](http://isis-data.science.uva.nl/hale/341n143/vkitti/flo_gt.zip),
    [predicted (52 GB)](http://isis-data.science.uva.nl/hale/341n143/vkitti/flo_pr.zip),
  - Semantic segmentation
    [ground truth (151 MB)](http://isis-data.science.uva.nl/hale/341n143/vkitti/sem_gt.zip),
    [predicted (315 GB)](http://isis-data.science.uva.nl/hale/341n143/vkitti/sem_pr.zip),
  - Surface normals
    [ground truth (63 GB)](http://isis-data.science.uva.nl/hale/341n143/vkitti/nrm_gt.zip),
    [predicted (75 GB)](http://isis-data.science.uva.nl/hale/341n143/vkitti/nrm_pr.zip),
- Nature
  - Optical flow:
    [ground truth (32 GB)](http://isis-data.science.uva.nl/hale/341n143/nature/flo_gt.zip),
    [predicted (15 GB)](http://isis-data.science.uva.nl/hale/341n143/nature/flo_pr.zip),
  - Semantic segmentation
    [ground truth (114 MB)](http://isis-data.science.uva.nl/hale/341n143/nature/sem_gt.zip),
    [predicted (107 GB)](http://isis-data.science.uva.nl/hale/341n143/nature/sem_pr.zip),
  - Surface normals
    [ground truth (37 GB)](http://isis-data.science.uva.nl/hale/341n143/nature/nrm_gt.zip),
    [predicted (27 GB)](http://isis-data.science.uva.nl/hale/341n143/nature/nrm_pr.zip),


## Installation

Build caffe 


## Naming convention

Each run is named in the following format

```
   [data]-[target]-[input],
```

where
- `[data]` is either `gdextracted` for the Nature dataset or `vkitti` for the
Virtual KITTI dataset.
- `[target]` is the target modality, written with `rf_` prefix, e.g. `rf_flow`
indicates the experiment to refine optical flow modality.
- `[input]` is the input branch configuration
  - `gt` indicates ground truth modalities and `pr` the predicteds.
  - the target modality is always written first and with predicted modality `pr`
  - underscores `_` indicate that the modalities are concatenated along the
depth channels
  - hyphens `-` indicate that the modalities are separated in different input
branches
- The supported modalities include
  - `flow` for optical flow
  - `seg` for semantic segmentation
  - `norm` for surface normal

## Training

### Re-producing the paper results

You can either call caffe train command directly using the prototxts in the
runs directory or use our python wrapper

### Training on new datasets

## Citation

