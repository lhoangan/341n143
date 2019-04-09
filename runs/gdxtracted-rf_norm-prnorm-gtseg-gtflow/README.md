### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-gtseg-gtflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-gtseg-gtflow/gdxtracted-rf_norm-prnorm-gtseg-gtflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-gtseg-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-gtseg-gtflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-gtseg-gtflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-gtseg-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-gtseg-gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.1786 | 7.3636 | 12.8238 | 64.1509 | 90.6317 | 97.4110
