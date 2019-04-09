### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_gtseg_gtflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_gtseg_gtflow/gdxtracted-rf_norm-prnorm_gtseg_gtflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_gtseg_gtflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_gtseg_gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.1035 | 7.1404 | 12.7515 | 64.6965 | 90.7630 | 97.4106
