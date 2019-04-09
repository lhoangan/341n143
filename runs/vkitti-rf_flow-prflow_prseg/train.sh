set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/vkitti-rf_flow-prflow_prseg/solver.pt --log_file ../output/vkitti-rf_flow-prflow_prseg/log_vkitti-rf_flow-prflow_prseg --blobs prflow_in prseg_in flow_gt out-flow --vis_path ../runs/vkitti-rf_flow-prflow_prseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_flow-prflow_prseg/log_vkitti-rf_flow-prflow_prseg

cp ../models/vkitti-rf_flow-prflow_prseg/vkitti-rf_flow-prflow_prseg_iter_200000.caffemodel ../runs/vkitti-rf_flow-prflow_prseg/vkitti-rf_flow-prflow_prseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_flow-prflow_prseg.yaml --proto ../runs/vkitti-rf_flow-prflow_prseg/test.pt --weight ../models/vkitti-rf_flow-prflow_prseg/vkitti-rf_flow-prflow_prseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_flow-prflow_prseg --out_blobs out-flow --perimg ../runs/vkitti-rf_flow-prflow_prseg/perimg.md --report ../runs/vkitti-rf_flow-prflow_prseg/README.md
