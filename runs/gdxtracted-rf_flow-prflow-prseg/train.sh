set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/gdxtracted-rf_flow-prflow-prseg/solver.pt --log_file ../output/gdxtracted-rf_flow-prflow-prseg/log_gdxtracted-rf_flow-prflow-prseg --blobs prflow_in prseg_in flow_gt out-flow --vis_path ../runs/gdxtracted-rf_flow-prflow-prseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_flow-prflow-prseg/log_gdxtracted-rf_flow-prflow-prseg

cp ../models/gdxtracted-rf_flow-prflow-prseg/gdxtracted-rf_flow-prflow-prseg_iter_200000.caffemodel ../runs/gdxtracted-rf_flow-prflow-prseg/gdxtracted-rf_flow-prflow-prseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_flow-prflow-prseg.yaml --proto ../runs/gdxtracted-rf_flow-prflow-prseg/test.pt --weight ../models/gdxtracted-rf_flow-prflow-prseg/gdxtracted-rf_flow-prflow-prseg_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_flow-prflow-prseg --out_blobs out-flow --perimg ../runs/gdxtracted-rf_flow-prflow-prseg/perimg.md --report ../runs/gdxtracted-rf_flow-prflow-prseg/README.md
