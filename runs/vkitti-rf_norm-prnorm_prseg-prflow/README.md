### Testing network
- *experiment* : vkitti-rf_norm-prnorm_prseg-prflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_prseg-prflow/vkitti-rf_norm-prnorm_prseg-prflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_prseg-prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_prseg-prflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_prseg-prflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_prseg-prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_prseg-prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.4435 | 2.8719 | 17.1972 | 60.0903 | 74.4775 | 86.0924
