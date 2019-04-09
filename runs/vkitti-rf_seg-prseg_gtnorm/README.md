### Testing network
- *experiment* : vkitti-rf_seg-prseg_gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg_gtnorm/vkitti-rf_seg-prseg_gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg_gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg_gtnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg_gtnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg_gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg_gtnorm

global | class | miou
------ | ----- | ----
0.8887 | 0.6232 | 0.5034

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
