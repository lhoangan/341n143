### Testing network
- *experiment* : gdxtracted-rf_seg-prseg_gtflow_gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg_gtflow_gtnorm/gdxtracted-rf_seg-prseg_gtflow_gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg_gtflow_gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg_gtflow_gtnorm/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg_gtflow_gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg_gtflow_gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg_gtflow_gtnorm

global | class | miou
------ | ----- | ----
0.7884 | 0.5812 | 0.4573

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
