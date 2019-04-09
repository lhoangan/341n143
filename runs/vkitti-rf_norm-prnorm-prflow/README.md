### Testing network
- *experiment* : vkitti-rf_norm-prnorm-prflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-prflow/vkitti-rf_norm-prnorm-prflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-prflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-prflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
12.2846 | 4.0913 | 18.0499 | 58.3663 | 73.2340 | 83.8354
