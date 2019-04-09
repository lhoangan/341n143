### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-gtseg_gtflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-gtseg_gtflow/gdxtracted-rf_norm-prnorm-gtseg_gtflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-gtseg_gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-gtseg_gtflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-gtseg_gtflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-gtseg_gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-gtseg_gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.0288 | 7.1441 | 12.5671 | 65.0810 | 91.2323 | 97.6499
