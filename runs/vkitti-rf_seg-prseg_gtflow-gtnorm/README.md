### Testing network
- *experiment* : vkitti-rf_seg-prseg_gtflow-gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg_gtflow-gtnorm/vkitti-rf_seg-prseg_gtflow-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg_gtflow-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg_gtflow-gtnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg_gtflow-gtnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg_gtflow-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg_gtflow-gtnorm

global | class | miou
------ | ----- | ----
0.8847 | 0.6113 | 0.4965

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
