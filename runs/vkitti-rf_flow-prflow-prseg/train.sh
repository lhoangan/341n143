set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_flow-prflow-prseg/solver.pt --log_file ../output/vkitti-rf_flow-prflow-prseg/log_vkitti-rf_flow-prflow-prseg --blobs prflow_in prseg_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow-prseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow-prseg/log_vkitti-rf_flow-prflow-prseg

cp ../models/vkitti-rf_flow-prflow-prseg/vkitti-rf_flow-prflow-prseg_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow-prseg/vkitti-rf_flow-prflow-prseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow-prseg.yaml --proto ../runs/vkitti-rf_flow-prflow-prseg/test.pt --weight ../models/vkitti-rf_flow-prflow-prseg/vkitti-rf_flow-prflow-prseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow-prseg --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow-prseg/perimg.md --report ../runs/vkitti-rf_flow-prflow-prseg/README.md
