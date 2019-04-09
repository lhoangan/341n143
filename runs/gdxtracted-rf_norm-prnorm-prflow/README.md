### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-prflow/gdxtracted-rf_norm-prnorm-prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-prflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-prflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.3305 | 9.7647 | 14.3321 | 55.6086 | 87.0189 | 96.7117
