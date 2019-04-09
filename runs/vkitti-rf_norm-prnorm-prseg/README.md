### Testing network
- *experiment* : vkitti-rf_norm-prnorm-prseg
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-prseg/vkitti-rf_norm-prnorm-prseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-prseg/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-prseg.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-prseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.4301 | 2.7093 | 17.2173 | 60.4861 | 74.3421 | 86.6781
