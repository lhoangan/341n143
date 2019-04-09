### Testing network
- *experiment* : vkitti-rf_seg-prseg-gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg-gtnorm/vkitti-rf_seg-prseg-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg-gtnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg-gtnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg-gtnorm

global | class | miou
------ | ----- | ----
0.8924 | 0.6245 | 0.5112

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
