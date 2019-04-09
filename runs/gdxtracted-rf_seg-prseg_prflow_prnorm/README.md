### Testing network
- *experiment* : gdxtracted-rf_seg-prseg_prflow_prnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg_prflow_prnorm/gdxtracted-rf_seg-prseg_prflow_prnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg_prflow_prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg_prflow_prnorm/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg_prflow_prnorm.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg_prflow_prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg_prflow_prnorm

global | class | miou
------ | ----- | ----
0.7812 | 0.5786 | 0.4517

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
