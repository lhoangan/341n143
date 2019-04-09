set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/gdxtracted-rf_flow-prflow-gtseg/solver.pt --log_file ../output/gdxtracted-rf_flow-prflow-gtseg/log_gdxtracted-rf_flow-prflow-gtseg --blobs prflow_in gtseg_in flow_gt out-flow --vis_path ../runs/gdxtracted-rf_flow-prflow-gtseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_flow-prflow-gtseg/log_gdxtracted-rf_flow-prflow-gtseg

cp ../models/gdxtracted-rf_flow-prflow-gtseg/gdxtracted-rf_flow-prflow-gtseg_iter_200000.caffemodel ../runs/gdxtracted-rf_flow-prflow-gtseg/gdxtracted-rf_flow-prflow-gtseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_flow-prflow-gtseg.yaml --proto ../runs/gdxtracted-rf_flow-prflow-gtseg/test.pt --weight ../models/gdxtracted-rf_flow-prflow-gtseg/gdxtracted-rf_flow-prflow-gtseg_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_flow-prflow-gtseg --out_blobs out-flow --perimg ../runs/gdxtracted-rf_flow-prflow-gtseg/perimg.md --report ../runs/gdxtracted-rf_flow-prflow-gtseg/README.md
