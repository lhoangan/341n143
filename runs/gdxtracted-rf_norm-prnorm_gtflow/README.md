### Testing network
- *experiment* : gdxtracted-rf_norm-prnorm_gtflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_norm-prnorm_gtflow/gdxtracted-rf_norm-prnorm_gtflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_norm-prnorm_gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_norm-prnorm_gtflow/perimg.md
- *common* : ../runs/gdxtracted_norm.md
- *exp* : ../experiments/gdxtracted-rf_norm-prnorm_gtflow.yaml
- *report* : ../runs/gdxtracted-rf_norm-prnorm_gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-norm']
- *outdir* : ../output/gdxtracted-rf_norm-prnorm_gtflow

mean | median | rmse | 11.25 | 22.5 | 30
---- | ------ | ---- | ----- | ---- | --
9.6713 | 8.0476 | 13.2965 | 61.4611 | 89.4938 | 97.3768
