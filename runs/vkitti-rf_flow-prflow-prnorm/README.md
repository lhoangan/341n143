### Testing network
- *experiment* : vkitti-rf_flow-prflow-prnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow-prnorm/vkitti-rf_flow-prflow-prnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow-prnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow-prnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow-prnorm

epe | aae
--- | ---
2.2287 | 12.2506
