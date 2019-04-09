### Testing network
- *experiment* : vkitti-rf_norm-prnorm-gtseg-gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-gtseg-gtflow/vkitti-rf_norm-prnorm-gtseg-gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-gtseg-gtflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-gtseg-gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
10.6360 | 3.5201 | 16.1024 | 62.3236 | 79.6800 | 89.9853
