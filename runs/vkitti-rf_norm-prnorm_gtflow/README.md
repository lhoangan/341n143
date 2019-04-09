### Testing network
- *experiment* : vkitti-rf_norm-prnorm_gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_gtflow/vkitti-rf_norm-prnorm_gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_gtflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_gtflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.4677 | 3.3874 | 17.2536 | 60.4426 | 76.6269 | 87.9240
