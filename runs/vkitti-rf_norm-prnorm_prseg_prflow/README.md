### Testing network
- *experiment* : vkitti-rf_norm-prnorm_prseg_prflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_prseg_prflow/vkitti-rf_norm-prnorm_prseg_prflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_prseg_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_prseg_prflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_prseg_prflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_prseg_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_prseg_prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.5483 | 3.1823 | 17.2339 | 59.9441 | 74.6338 | 86.0030
