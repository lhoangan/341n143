### Testing network
- *experiment* : gdxtracted-rf_flow-prflow_prnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow_prnorm/gdxtracted-rf_flow-prflow_prnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow_prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow_prnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow_prnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow_prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow_prnorm

epe | aae
--- | ---
17.4525 | 18.7334
