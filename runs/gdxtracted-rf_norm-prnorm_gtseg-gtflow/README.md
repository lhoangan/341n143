### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_gtseg-gtflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_gtseg-gtflow/gdxtracted-rf_norm-prnorm_gtseg-gtflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_gtseg-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_gtseg-gtflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_gtseg-gtflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_gtseg-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_gtseg-gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.1469 | 7.2694 | 12.8274 | 64.7383 | 90.8332 | 97.2836
