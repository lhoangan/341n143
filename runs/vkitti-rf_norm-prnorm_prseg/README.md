### Testing network
- *experiment* : vkitti-rf_norm-prnorm_prseg
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_prseg/vkitti-rf_norm-prnorm_prseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_prseg/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_prseg.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_prseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.4677 | 2.9293 | 17.2230 | 60.2849 | 74.0208 | 86.6414
