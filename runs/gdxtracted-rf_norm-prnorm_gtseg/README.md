### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_gtseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_gtseg/gdxtracted-rf_norm-prnorm_gtseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_gtseg/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_gtseg.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_gtseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
8.4871 | 6.4064 | 11.9774 | 68.3289 | 92.3611 | 97.8630
