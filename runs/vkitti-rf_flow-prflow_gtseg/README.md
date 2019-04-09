### Testing network
- *experiment* : vkitti-rf_flow-prflow_gtseg
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow_gtseg/vkitti-rf_flow-prflow_gtseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow_gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow_gtseg/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow_gtseg.yaml
- *report* : ../runs/vkitti-rf_flow-prflow_gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow_gtseg

epe | aae
--- | ---
2.0746 | 10.2406
