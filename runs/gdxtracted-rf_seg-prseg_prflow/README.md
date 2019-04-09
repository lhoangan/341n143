### Testing network
- *experiment* : gdxtracted-rf_seg-prseg_prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg_prflow/gdxtracted-rf_seg-prseg_prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg_prflow/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg_prflow.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg_prflow

global | class | miou
------ | ----- | ----
0.7791 | 0.5717 | 0.4460

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
