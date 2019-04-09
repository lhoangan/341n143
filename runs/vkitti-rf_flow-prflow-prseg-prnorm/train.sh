set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/vkitti-rf_flow-prflow-prseg-prnorm/solver.pt --log_file ../output/vkitti-rf_flow-prflow-prseg-prnorm/log_vkitti-rf_flow-prflow-prseg-prnorm --blobs prflow_in prseg_in prnorm_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow-prseg-prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow-prseg-prnorm/log_vkitti-rf_flow-prflow-prseg-prnorm

cp ../models/vkitti-rf_flow-prflow-prseg-prnorm/vkitti-rf_flow-prflow-prseg-prnorm_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow-prseg-prnorm/vkitti-rf_flow-prflow-prseg-prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow-prseg-prnorm.yaml --proto ../runs/vkitti-rf_flow-prflow-prseg-prnorm/test.pt --weight ../models/vkitti-rf_flow-prflow-prseg-prnorm/vkitti-rf_flow-prflow-prseg-prnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow-prseg-prnorm --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow-prseg-prnorm/perimg.md --report ../runs/vkitti-rf_flow-prflow-prseg-prnorm/README.md
