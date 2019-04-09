set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/vkitti-rf_flow-prflow-gtseg/solver.pt --log_file ../output/vkitti-rf_flow-prflow-gtseg/log_vkitti-rf_flow-prflow-gtseg --blobs prflow_in gtseg_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow-gtseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow-gtseg/log_vkitti-rf_flow-prflow-gtseg

cp ../models/vkitti-rf_flow-prflow-gtseg/vkitti-rf_flow-prflow-gtseg_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow-gtseg/vkitti-rf_flow-prflow-gtseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow-gtseg.yaml --proto ../runs/vkitti-rf_flow-prflow-gtseg/test.pt --weight ../models/vkitti-rf_flow-prflow-gtseg/vkitti-rf_flow-prflow-gtseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow-gtseg --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow-gtseg/perimg.md --report ../runs/vkitti-rf_flow-prflow-gtseg/README.md
