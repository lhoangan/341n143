### Testing network
- *experiment* : gdxtracted-rf_seg-prseg-gtflow
- *palette* : None
- *weight* : ../models/gdxtracted-rf_seg-prseg-gtflow/gdxtracted-rf_seg-prseg-gtflow_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_seg-prseg-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_seg-prseg-gtflow/perimg.md
- *common* : ../runs/gdxtracted_seg.md
- *exp* : ../experiments/gdxtracted-rf_seg-prseg-gtflow.yaml
- *report* : ../runs/gdxtracted-rf_seg-prseg-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/gdxtracted-rf_seg-prseg-gtflow

global | class | miou
------ | ----- | ----
0.7871 | 0.5750 | 0.4527

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
