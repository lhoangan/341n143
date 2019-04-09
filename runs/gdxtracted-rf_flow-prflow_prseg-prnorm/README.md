### Testing network
- *experiment* : gdxtracted-rf_flow-prflow_prseg-prnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow_prseg-prnorm/gdxtracted-rf_flow-prflow_prseg-prnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow_prseg-prnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow_prseg-prnorm

epe | aae
--- | ---
13.1436 | 8.0395
