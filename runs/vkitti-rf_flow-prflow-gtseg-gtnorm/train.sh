set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/solver.pt --log_file ../output/vkitti-rf_flow-prflow-gtseg-gtnorm/log_vkitti-rf_flow-prflow-gtseg-gtnorm --blobs prflow_in gtseg_in gtnorm_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow-gtseg-gtnorm/log_vkitti-rf_flow-prflow-gtseg-gtnorm

cp ../models/vkitti-rf_flow-prflow-gtseg-gtnorm/vkitti-rf_flow-prflow-gtseg-gtnorm_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/vkitti-rf_flow-prflow-gtseg-gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow-gtseg-gtnorm.yaml --proto ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/test.pt --weight ../models/vkitti-rf_flow-prflow-gtseg-gtnorm/vkitti-rf_flow-prflow-gtseg-gtnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow-gtseg-gtnorm --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/perimg.md --report ../runs/vkitti-rf_flow-prflow-gtseg-gtnorm/README.md
