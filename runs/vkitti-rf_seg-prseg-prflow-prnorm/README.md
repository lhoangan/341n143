### Testing network
- *experiment* : vkitti-rf_seg-prseg-prflow-prnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg-prflow-prnorm/vkitti-rf_seg-prseg-prflow-prnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg-prflow-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg-prflow-prnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg-prflow-prnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg-prflow-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg-prflow-prnorm

global | class | miou
------ | ----- | ----
0.8553 | 0.5410 | 0.4455

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
