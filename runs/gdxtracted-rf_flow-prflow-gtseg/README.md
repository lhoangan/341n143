### Testing network
- *experiment* : gdxtracted-rf_flow-prflow-gtseg
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow-gtseg/gdxtracted-rf_flow-prflow-gtseg_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow-gtseg/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow-gtseg/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow-gtseg.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow-gtseg/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow-gtseg

epe | aae
--- | ---
12.1662 | 6.3351
