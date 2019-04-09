### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_prflow/gdxtracted-rf_norm-prnorm_prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_prflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_prflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
11.4233 | 9.7426 | 14.3782 | 55.5959 | 86.8629 | 96.6473
