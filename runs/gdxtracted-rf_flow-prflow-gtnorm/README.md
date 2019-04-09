### Testing network
- *experiment* : gdxtracted-rf_flow-prflow-gtnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow-gtnorm/gdxtracted-rf_flow-prflow-gtnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow-gtnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow-gtnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow-gtnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow-gtnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow-gtnorm

epe | aae
--- | ---
12.2802 | 6.6360
