### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_prseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_prseg/gdxtracted-rf_norm-prnorm_prseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_prseg/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_prseg.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_prseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
8.9956 | 7.0050 | 12.4375 | 65.7894 | 91.4518 | 97.7558
