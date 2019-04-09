### Testing network
- *experiment* : gdxtracted-rf_flow-prflow-prseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow-prseg/gdxtracted-rf_flow-prflow-prseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow-prseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow-prseg/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow-prseg.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow-prseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow-prseg

epe | aae
--- | ---
12.4111 | 6.7860
