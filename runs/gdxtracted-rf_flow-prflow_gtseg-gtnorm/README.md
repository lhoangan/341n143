### Testing network
- *experiment* : gdxtracted-rf_flow-prflow_gtseg-gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow_gtseg-gtnorm/gdxtracted-rf_flow-prflow_gtseg-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow_gtseg-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow_gtseg-gtnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow_gtseg-gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow_gtseg-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow_gtseg-gtnorm

epe | aae
--- | ---
12.7242 | 7.7190
