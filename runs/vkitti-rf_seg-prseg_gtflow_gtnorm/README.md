### Testing network
- *experiment* : vkitti-rf_seg-prseg_gtflow_gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg_gtflow_gtnorm/vkitti-rf_seg-prseg_gtflow_gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg_gtflow_gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg_gtflow_gtnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg_gtflow_gtnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg_gtflow_gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg_gtflow_gtnorm

global | class | miou
------ | ----- | ----
0.8795 | 0.5766 | 0.4746

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
