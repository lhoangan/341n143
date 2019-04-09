set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/vkitti-rf_flow-prflow-gtnorm/solver.pt --log_file ../output/vkitti-rf_flow-prflow-gtnorm/log_vkitti-rf_flow-prflow-gtnorm --blobs prflow_in gtnorm_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow-gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow-gtnorm/log_vkitti-rf_flow-prflow-gtnorm

cp ../models/vkitti-rf_flow-prflow-gtnorm/vkitti-rf_flow-prflow-gtnorm_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow-gtnorm/vkitti-rf_flow-prflow-gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow-gtnorm.yaml --proto ../runs/vkitti-rf_flow-prflow-gtnorm/test.pt --weight ../models/vkitti-rf_flow-prflow-gtnorm/vkitti-rf_flow-prflow-gtnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow-gtnorm --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow-gtnorm/perimg.md --report ../runs/vkitti-rf_flow-prflow-gtnorm/README.md
