### Testing network
- *experiment* : vkitti-rf_seg-prseg-gtflow-gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg-gtflow-gtnorm/vkitti-rf_seg-prseg-gtflow-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg-gtflow-gtnorm.yaml
- *report* : ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg-gtflow-gtnorm

global | class | miou
------ | ----- | ----
0.8841 | 0.6077 | 0.4910

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
