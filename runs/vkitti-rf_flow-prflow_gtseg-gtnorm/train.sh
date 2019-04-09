set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/solver.pt --log_file ../output/vkitti-rf_flow-prflow_gtseg-gtnorm/log_vkitti-rf_flow-prflow_gtseg-gtnorm --blobs prflow_in gtseg_in gtnorm_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow_gtseg-gtnorm/log_vkitti-rf_flow-prflow_gtseg-gtnorm

cp ../models/vkitti-rf_flow-prflow_gtseg-gtnorm/vkitti-rf_flow-prflow_gtseg-gtnorm_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/vkitti-rf_flow-prflow_gtseg-gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow_gtseg-gtnorm.yaml --proto ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/test.pt --weight ../models/vkitti-rf_flow-prflow_gtseg-gtnorm/vkitti-rf_flow-prflow_gtseg-gtnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow_gtseg-gtnorm --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/perimg.md --report ../runs/vkitti-rf_flow-prflow_gtseg-gtnorm/README.md
