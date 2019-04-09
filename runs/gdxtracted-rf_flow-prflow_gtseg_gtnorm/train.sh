set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/gdxtracted-rf_flow-prflow_gtseg_gtnorm/solver.pt --log_file ../output/gdxtracted-rf_flow-prflow_gtseg_gtnorm/log_gdxtracted-rf_flow-prflow_gtseg_gtnorm --blobs prflow_in gtseg_in gtnorm_in flow_gt out-flow --vis_path ../runs/gdxtracted-rf_flow-prflow_gtseg_gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_flow-prflow_gtseg_gtnorm/log_gdxtracted-rf_flow-prflow_gtseg_gtnorm

cp ../models/gdxtracted-rf_flow-prflow_gtseg_gtnorm/gdxtracted-rf_flow-prflow_gtseg_gtnorm_iter_200000.caffemodel ../runs/gdxtracted-rf_flow-prflow_gtseg_gtnorm/gdxtracted-rf_flow-prflow_gtseg_gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_flow-prflow_gtseg_gtnorm.yaml --proto ../runs/gdxtracted-rf_flow-prflow_gtseg_gtnorm/test.pt --weight ../models/gdxtracted-rf_flow-prflow_gtseg_gtnorm/gdxtracted-rf_flow-prflow_gtseg_gtnorm_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_flow-prflow_gtseg_gtnorm --out_blobs out-flow --perimg ../runs/gdxtracted-rf_flow-prflow_gtseg_gtnorm/perimg.md --report ../runs/gdxtracted-rf_flow-prflow_gtseg_gtnorm/README.md
