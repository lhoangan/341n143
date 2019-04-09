### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-prseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-prseg/gdxtracted-rf_norm-prnorm-prseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-prseg/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-prseg.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-prseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
8.9504 | 6.9049 | 12.3967 | 66.0251 | 91.5187 | 97.7996
