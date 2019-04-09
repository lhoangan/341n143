### Testing network
- *experiment* : gdxtracted-rf_seg-prseg-gtflow-gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg-gtflow-gtnorm/gdxtracted-rf_seg-prseg-gtflow-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg-gtflow-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg-gtflow-gtnorm/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg-gtflow-gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg-gtflow-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg-gtflow-gtnorm

global | class | miou
------ | ----- | ----
0.7946 | 0.5839 | 0.4652

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
