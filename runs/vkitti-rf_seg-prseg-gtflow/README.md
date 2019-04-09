### Testing network
- *experiment* : vkitti-rf_seg-prseg-gtflow
- *palette* : None
- *weight* : ../models/vkitti-rf_seg-prseg-gtflow/vkitti-rf_seg-prseg-gtflow_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_seg-prseg-gtflow/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_seg-prseg-gtflow/perimg.md
- *common* : ../runs/vkitti_seg.md
- *exp* : ../experiments/vkitti-rf_seg-prseg-gtflow.yaml
- *report* : ../runs/vkitti-rf_seg-prseg-gtflow/README.md
- *gpu* : 0
- *out_blobs* : ['out-seg']
- *outdir* : ../output/vkitti-rf_seg-prseg-gtflow

global | class | miou
------ | ----- | ----
0.8718 | 0.5627 | 0.4673

- *Confusion matrix* : False Negative | False Positive

![conf_mat_fn](confmat_fn.png) | ![conf_mat_fp](confmat_fp.png)
