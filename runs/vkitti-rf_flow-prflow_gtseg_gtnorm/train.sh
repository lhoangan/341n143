set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/solver.pt --log_file ../output/vkitti-rf_flow-prflow_gtseg_gtnorm/log_vkitti-rf_flow-prflow_gtseg_gtnorm --blobs prflow_in gtseg_in gtnorm_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow_gtseg_gtnorm/log_vkitti-rf_flow-prflow_gtseg_gtnorm

cp ../models/vkitti-rf_flow-prflow_gtseg_gtnorm/vkitti-rf_flow-prflow_gtseg_gtnorm_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/vkitti-rf_flow-prflow_gtseg_gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow_gtseg_gtnorm.yaml --proto ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/test.pt --weight ../models/vkitti-rf_flow-prflow_gtseg_gtnorm/vkitti-rf_flow-prflow_gtseg_gtnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow_gtseg_gtnorm --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/perimg.md --report ../runs/vkitti-rf_flow-prflow_gtseg_gtnorm/README.md
