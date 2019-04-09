### Testing network
- *experiment* : vkitti-rf_norm-prnorm-prseg-prflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-prseg-prflow/vkitti-rf_norm-prnorm-prseg-prflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-prseg-prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-prseg-prflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-prseg-prflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-prseg-prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-prseg-prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.6650 | 3.9816 | 17.2609 | 59.6502 | 74.6964 | 86.4785
