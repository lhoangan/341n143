### Testing network
- *experiment* : vkitti-rf_norm-prnorm_prflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_prflow/vkitti-rf_norm-prnorm_prflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_prflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_prflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
12.3525 | 4.5114 | 18.0779 | 58.0927 | 73.2068 | 83.9588
