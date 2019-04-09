### Testing network
- *experiment* : vkitti-rf_norm-prnorm-gtseg
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-gtseg/vkitti-rf_norm-prnorm-gtseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-gtseg/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-gtseg.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-gtseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
10.9893 | 2.9743 | 16.5479 | 61.3303 | 76.5126 | 89.2187
