### Testing network
- *experiment* : gdxtracted-rf_seg-prseg-prflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg-prflow/gdxtracted-rf_seg-prseg-prflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg-prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg-prflow/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg-prflow.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg-prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg-prflow

global | class | miou
------ | ----- | ----
0.7823 | 0.5756 | 0.4529

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
