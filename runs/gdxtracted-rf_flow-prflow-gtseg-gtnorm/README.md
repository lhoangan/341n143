### Testing network
- *experiment* : gdxtracted-rf_flow-prflow-gtseg-gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow-gtseg-gtnorm/gdxtracted-rf_flow-prflow-gtseg-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow-gtseg-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow-gtseg-gtnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow-gtseg-gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow-gtseg-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow-gtseg-gtnorm

epe | aae
--- | ---
12.5052 | 6.9475
