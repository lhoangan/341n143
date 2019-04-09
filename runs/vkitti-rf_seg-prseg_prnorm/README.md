### Testing network
- *experiment* : vkitti-rf_seg-prseg_prnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg_prnorm/vkitti-rf_seg-prseg_prnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg_prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg_prnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg_prnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg_prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg_prnorm

global | class | miou
------ | ----- | ----
0.8573 | 0.5509 | 0.4535

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
