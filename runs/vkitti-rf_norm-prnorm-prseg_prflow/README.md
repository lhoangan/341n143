### Testing network
- *experiment* : vkitti-rf_norm-prnorm-prseg_prflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-prseg_prflow/vkitti-rf_norm-prnorm-prseg_prflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-prseg_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-prseg_prflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-prseg_prflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-prseg_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-prseg_prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.6452 | 3.3804 | 17.2758 | 59.2917 | 74.6663 | 86.5110
