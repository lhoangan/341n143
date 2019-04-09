### Testing network
- *experiment* : vkitti-rf_flow-prflow-prseg-prnorm
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow-prseg-prnorm/vkitti-rf_flow-prflow-prseg-prnorm_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow-prseg-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow-prseg-prnorm/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow-prseg-prnorm.yaml
- *report* : ../runs/vkitti-rf_flow-prflow-prseg-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow-prseg-prnorm

epe | aae
--- | ---
2.1408 | 10.6731
