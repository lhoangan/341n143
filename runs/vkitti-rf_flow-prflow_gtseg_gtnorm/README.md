### Testing network
- *experiment* : vkitti-rf_flow-prflow_gtseg_gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow_gtseg_gtnorm/vkitti-rf_flow-prflow_gtseg_gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow_gtseg_gtnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow_gtseg_gtnorm

epe | aae
--- | ---
2.0609 | 10.2321
