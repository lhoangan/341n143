### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-prseg-prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-prseg-prflow/gdxtracted-rf_norm-prnorm-prseg-prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-prseg-prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-prseg-prflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-prseg-prflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-prseg-prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-prseg-prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.2899 | 7.5029 | 12.8543 | 63.5812 | 90.5121 | 97.5683
