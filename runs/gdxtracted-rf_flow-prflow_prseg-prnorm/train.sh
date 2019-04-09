set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/solver.pt --log_file ../output/gdxtracted-rf_flow-prflow_prseg-prnorm/log_gdxtracted-rf_flow-prflow_prseg-prnorm --blobs prflow_in prseg_in prnorm_in flow_gt out-flow --vis_path ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_flow-prflow_prseg-prnorm/log_gdxtracted-rf_flow-prflow_prseg-prnorm

cp ../models/gdxtracted-rf_flow-prflow_prseg-prnorm/gdxtracted-rf_flow-prflow_prseg-prnorm_iter_200000.caffemodel ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/gdxtracted-rf_flow-prflow_prseg-prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_flow-prflow_prseg-prnorm.yaml --proto ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/test.pt --weight ../models/gdxtracted-rf_flow-prflow_prseg-prnorm/gdxtracted-rf_flow-prflow_prseg-prnorm_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_flow-prflow_prseg-prnorm --out_blobs out-flow --perimg ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/perimg.md --report ../runs/gdxtracted-rf_flow-prflow_prseg-prnorm/README.md
