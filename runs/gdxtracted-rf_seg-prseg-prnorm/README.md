### Testing network
- *experiment* : gdxtracted-rf_seg-prseg-prnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg-prnorm/gdxtracted-rf_seg-prseg-prnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg-prnorm/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg-prnorm.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg-prnorm

global | class | miou
------ | ----- | ----
0.7847 | 0.5754 | 0.4525

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
