### Testing network
- *experiment* : gdxtracted-rf_seg-prseg-gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg-gtnorm/gdxtracted-rf_seg-prseg-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg-gtnorm/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg-gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg-gtnorm

global | class | miou
------ | ----- | ----
0.8059 | 0.6057 | 0.4847

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
