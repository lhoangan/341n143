### Testing network
- *experiment* : gdxtracted-rf_seg-prseg-prflow-prnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg-prflow-prnorm/gdxtracted-rf_seg-prseg-prflow-prnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg-prflow-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg-prflow-prnorm/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg-prflow-prnorm.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg-prflow-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg-prflow-prnorm

global | class | miou
------ | ----- | ----
0.7819 | 0.5723 | 0.4502

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
