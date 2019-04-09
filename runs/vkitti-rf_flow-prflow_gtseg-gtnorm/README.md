### Testing network
- *experiment* : vkitti-rf_flow-prflow_gtseg-gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow_gtseg-gtnorm/vkitti-rf_flow-prflow_gtseg-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow_gtseg-gtnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow_gtseg-gtnorm

epe | aae
--- | ---
2.0645 | 10.3743
