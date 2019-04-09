### Testing network
- *experiment* : vkitti-rf_norm-prnorm_gtseg_gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm_gtseg_gtflow/vkitti-rf_norm-prnorm_gtseg_gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm_gtseg_gtflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm_gtseg_gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
10.7937 | 3.1125 | 16.3736 | 62.1692 | 77.4652 | 89.4428
