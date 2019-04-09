### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-prseg_prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-prseg_prflow/gdxtracted-rf_norm-prnorm-prseg_prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-prseg_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-prseg_prflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-prseg_prflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-prseg_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-prseg_prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.3765 | 7.4553 | 12.8096 | 63.7444 | 90.6477 | 97.6276
