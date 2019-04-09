### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm-gtseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm-gtseg/gdxtracted-rf_norm-prnorm-gtseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm-gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm-gtseg/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm-gtseg.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm-gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm-gtseg

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
8.4917 | 6.3757 | 11.9557 | 68.5676 | 92.3286 | 97.8556
