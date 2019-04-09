### Testing network
- *experiment* : vkitti-rf_flow-prflow_prseg
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow_prseg/vkitti-rf_flow-prflow_prseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow_prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow_prseg/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow_prseg.yaml
- *report* : ../runs/vkitti-rf_flow-prflow_prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow_prseg

epe | aae
--- | ---
2.1358 | 10.8498
