### Testing network
- *experiment* : gdxtracted-rf_flow-prflow-gtseg_gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow-gtseg_gtnorm/gdxtracted-rf_flow-prflow-gtseg_gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow-gtseg_gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow-gtseg_gtnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow-gtseg_gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow-gtseg_gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow-gtseg_gtnorm

epe | aae
--- | ---
12.5245 | 6.9741
