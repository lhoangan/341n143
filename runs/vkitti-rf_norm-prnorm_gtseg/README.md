### Testing network
- *experiment* : vkitti-rf_norm-prnorm_gtseg
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_gtseg/vkitti-rf_norm-prnorm_gtseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_gtseg/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_gtseg.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_gtseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
10.8215 | 3.3127 | 16.3468 | 62.3069 | 77.4047 | 89.3943
