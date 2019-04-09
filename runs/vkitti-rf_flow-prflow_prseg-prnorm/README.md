### Testing network
- *experiment* : vkitti-rf_flow-prflow_prseg-prnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow_prseg-prnorm/vkitti-rf_flow-prflow_prseg-prnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow_prseg-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow_prseg-prnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow_prseg-prnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow_prseg-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow_prseg-prnorm

epe | aae
--- | ---
2.1439 | 10.7898
