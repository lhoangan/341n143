### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_prseg-prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_prseg-prflow/gdxtracted-rf_norm-prnorm_prseg-prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_prseg-prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_prseg-prflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_prseg-prflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_prseg-prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_prseg-prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.3369 | 7.4648 | 12.8935 | 63.6194 | 90.4302 | 97.4856
