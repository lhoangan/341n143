### Testing network
- *experiment* : vkitti-rf_seg-prseg_prflow
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg_prflow/vkitti-rf_seg-prseg_prflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg_prflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg_prflow/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg_prflow.yaml
- *report* : ../runs/vkitti-rf_seg-prseg_prflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg_prflow

global | class | miou
------ | ----- | ----
0.8527 | 0.5277 | 0.4341

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
