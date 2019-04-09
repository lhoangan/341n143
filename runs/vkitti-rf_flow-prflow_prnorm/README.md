### Testing network
- *experiment* : vkitti-rf_flow-prflow_prnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow_prnorm/vkitti-rf_flow-prflow_prnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow_prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow_prnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow_prnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow_prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow_prnorm

epe | aae
--- | ---
2.2155 | 12.3840
