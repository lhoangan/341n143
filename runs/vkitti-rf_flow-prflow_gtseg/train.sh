set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/vkitti-rf_flow-prflow_gtseg/solver.pt --log_file ../output/vkitti-rf_flow-prflow_gtseg/log_vkitti-rf_flow-prflow_gtseg --blobs prflow_in gtseg_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow_gtseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow_gtseg/log_vkitti-rf_flow-prflow_gtseg

cp ../models/vkitti-rf_flow-prflow_gtseg/vkitti-rf_flow-prflow_gtseg_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow_gtseg/vkitti-rf_flow-prflow_gtseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow_gtseg.yaml --proto ../runs/vkitti-rf_flow-prflow_gtseg/test.pt --weight ../models/vkitti-rf_flow-prflow_gtseg/vkitti-rf_flow-prflow_gtseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow_gtseg --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow_gtseg/perimg.md --report ../runs/vkitti-rf_flow-prflow_gtseg/README.md
