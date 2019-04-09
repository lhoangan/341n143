### Testing network
- *experiment* : gdxtracted-rf_flow-prflow-prnorm
- *palette* : None
- *weight* : ../models/gdxtracted-rf_flow-prflow-prnorm/gdxtracted-rf_flow-prflow-prnorm_iter_200000.caffemodel
- *proto* : ../runs/gdxtracted-rf_flow-prflow-prnorm/test.pt
- *config* : ../configs/general.yaml
- *perimg* : ../runs/gdxtracted-rf_flow-prflow-prnorm/perimg.md
- *common* : ../runs/gdxtracted_flow.md
- *exp* : ../experiments/gdxtracted-rf_flow-prflow-prnorm.yaml
- *report* : ../runs/gdxtracted-rf_flow-prflow-prnorm/README.md
- *gpu* : 0
- *out_blobs* : ['out-flow']
- *outdir* : ../output/gdxtracted-rf_flow-prflow-prnorm

epe | aae
--- | ---
15.4839 | 13.9553
