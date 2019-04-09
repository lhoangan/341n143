### Testing network
- *experiment* : gdxtracted-rf_flow-prflow_prseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow_prseg/gdxtracted-rf_flow-prflow_prseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow_prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow_prseg/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow_prseg.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow_prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow_prseg

epe | aae
--- | ---
14.4542 | 11.2597
