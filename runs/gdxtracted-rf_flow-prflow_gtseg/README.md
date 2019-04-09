### Testing network
- *experiment* : gdxtracted-rf_flow-prflow_gtseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow_gtseg/gdxtracted-rf_flow-prflow_gtseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow_gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow_gtseg/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow_gtseg.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow_gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow_gtseg

epe | aae
--- | ---
12.5471 | 7.2326
