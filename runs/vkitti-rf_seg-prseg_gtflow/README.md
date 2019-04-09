### Testing network
- *experiment* : vkitti-rf_seg-prseg_gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg_gtflow/vkitti-rf_seg-prseg_gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg_gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg_gtflow/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg_gtflow.yaml
- *report* : ../runs/vkitti-rf_seg-prseg_gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg_gtflow

global | class | miou
------ | ----- | ----
0.8706 | 0.5450 | 0.4537

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
