### Testing network
- *experiment* : vkitti-rf_norm-prnorm-gtseg_gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_norm-prnorm-gtseg_gtflow/vkitti-rf_norm-prnorm-gtseg_gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_norm-prnorm-gtseg_gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_norm-prnorm-gtseg_gtflow/perimg.md
- *common* : ../runs/vkitti_norm.md
- *exp* : ../experiments/vkitti-rf_norm-prnorm-gtseg_gtflow.yaml
- *report* : ../runs/vkitti-rf_norm-prnorm-gtseg_gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/vkitti-rf_norm-prnorm-gtseg_gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
10.6811 | 3.4182 | 16.0865 | 61.9627 | 79.7387 | 90.0772
