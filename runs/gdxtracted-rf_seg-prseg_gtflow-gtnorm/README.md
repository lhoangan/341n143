### Testing network
- *experiment* : gdxtracted-rf_seg-prseg_gtflow-gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg_gtflow-gtnorm/gdxtracted-rf_seg-prseg_gtflow-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg_gtflow-gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg_gtflow-gtnorm

global | class | miou
------ | ----- | ----
0.7953 | 0.5916 | 0.4709

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
