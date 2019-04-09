### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_prseg_prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_prseg_prflow/gdxtracted-rf_norm-prnorm_prseg_prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_prseg_prflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_prseg_prflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.3234 | 7.5438 | 12.9201 | 63.3842 | 90.3933 | 97.4515
