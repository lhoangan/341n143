set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/vkitti-rf_norm-prnorm-gtflow/solver.pt --log_file ../output/vkitti-rf_norm-prnorm-gtflow/log_vkitti-rf_norm-prnorm-gtflow --blobs prnorm_in gtflow_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm-gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm-gtflow/log_vkitti-rf_norm-prnorm-gtflow

cp ../models/vkitti-rf_norm-prnorm-gtflow/vkitti-rf_norm-prnorm-gtflow_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm-gtflow/vkitti-rf_norm-prnorm-gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm-gtflow.yaml --proto ../runs/vkitti-rf_norm-prnorm-gtflow/test.pt --weight ../models/vkitti-rf_norm-prnorm-gtflow/vkitti-rf_norm-prnorm-gtflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm-gtflow --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm-gtflow/perimg.md --report ../runs/vkitti-rf_norm-prnorm-gtflow/README.md
