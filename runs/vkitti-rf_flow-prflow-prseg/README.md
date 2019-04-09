### Testing network
- *experiment* : vkitti-rf_flow-prflow-prseg
- *palette* : None
- *weight* : ../models/vkitti-rf_flow-prflow-prseg/vkitti-rf_flow-prflow-prseg_iter_200000.caffemodel
- *proto* : ../runs/vkitti-rf_flow-prflow-prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/vkitti-rf_flow-prflow-prseg/perimg.md
- *common* : ../runs/vkitti_flow.md
- *exp* : ../experiments/vkitti-rf_flow-prflow-prseg.yaml
- *report* : ../runs/vkitti-rf_flow-prflow-prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/vkitti-rf_flow-prflow-prseg

epe | aae
--- | ---
2.1294 | 10.9278
