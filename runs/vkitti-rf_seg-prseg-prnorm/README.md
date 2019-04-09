### Testing network
- *experiment* : vkitti-rf_seg-prseg-prnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg-prnorm/vkitti-rf_seg-prseg-prnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg-prnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg-prnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg-prnorm

global | class | miou
------ | ----- | ----
0.8585 | 0.5518 | 0.4566

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
