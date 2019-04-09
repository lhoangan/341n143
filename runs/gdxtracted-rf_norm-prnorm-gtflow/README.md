### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-gtflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-gtflow/gdxtracted-rf_norm-prnorm-gtflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-gtflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-gtflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.7197 | 8.1151 | 13.3256 | 61.3465 | 89.3805 | 97.3679
