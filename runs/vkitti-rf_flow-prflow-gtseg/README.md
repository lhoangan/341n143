### Testing network
- *experiment* : vkitti-rf_flow-prflow-gtseg
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow-gtseg/vkitti-rf_flow-prflow-gtseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow-gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow-gtseg/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow-gtseg.yaml
- *report* : ../runs/vkitti-rf_flow-prflow-gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow-gtseg

epe | aae
--- | ---
2.0862 | 10.4583
