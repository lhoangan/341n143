### Testing network
- *experiment* : vkitti-rf_norm-prnorm-gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-gtflow/vkitti-rf_norm-prnorm-gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-gtflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-gtflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.0833 | 3.4942 | 16.9341 | 62.5813 | 77.7202 | 87.8095
