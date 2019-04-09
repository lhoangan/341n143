set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/gdxtracted-rf_flow-prflow_prnorm/solver.pt --log_file ../output/gdxtracted-rf_flow-prflow_prnorm/log_gdxtracted-rf_flow-prflow_prnorm --blobs prflow_in prnorm_in flow_gt out-flow --vis_path ../runs/gdxtracted-rf_flow-prflow_prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_flow-prflow_prnorm/log_gdxtracted-rf_flow-prflow_prnorm

cp ../models/gdxtracted-rf_flow-prflow_prnorm/gdxtracted-rf_flow-prflow_prnorm_iter_200000.caffemodel ../runs/gdxtracted-rf_flow-prflow_prnorm/gdxtracted-rf_flow-prflow_prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_flow-prflow_prnorm.yaml --proto ../runs/gdxtracted-rf_flow-prflow_prnorm/test.pt --weight ../models/gdxtracted-rf_flow-prflow_prnorm/gdxtracted-rf_flow-prflow_prnorm_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_flow-prflow_prnorm --out_blobs out-flow --perimg ../runs/gdxtracted-rf_flow-prflow_prnorm/perimg.md --report ../runs/gdxtracted-rf_flow-prflow_prnorm/README.md
