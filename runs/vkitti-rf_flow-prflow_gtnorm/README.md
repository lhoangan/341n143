### Testing network
- *experiment* : vkitti-rf_flow-prflow_gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow_gtnorm/vkitti-rf_flow-prflow_gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow_gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow_gtnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow_gtnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow_gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow_gtnorm

epe | aae
--- | ---
2.0878 | 10.3842
