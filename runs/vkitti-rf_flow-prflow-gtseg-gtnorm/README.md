### Testing network
- *experiment* : vkitti-rf_flow-prflow-gtseg-gtnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow-gtseg-gtnorm/vkitti-rf_flow-prflow-gtseg-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow-gtseg-gtnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow-gtseg-gtnorm

epe | aae
--- | ---
2.0666 | 10.3202
