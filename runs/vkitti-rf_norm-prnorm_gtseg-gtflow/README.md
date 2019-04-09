### Testing network
- *experiment* : vkitti-rf_norm-prnorm_gtseg-gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_gtseg-gtflow/vkitti-rf_norm-prnorm_gtseg-gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_gtseg-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_gtseg-gtflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_gtseg-gtflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_gtseg-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_gtseg-gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
10.6215 | 2.9187 | 16.1709 | 61.8713 | 79.3935 | 89.7143
