### Testing network
- *experiment* : gdxtracted-rf_flow-prflow-prseg-prnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow-prseg-prnorm/gdxtracted-rf_flow-prflow-prseg-prnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow-prseg-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow-prseg-prnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow-prseg-prnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow-prseg-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow-prseg-prnorm

epe | aae
--- | ---
12.4549 | 6.8629
