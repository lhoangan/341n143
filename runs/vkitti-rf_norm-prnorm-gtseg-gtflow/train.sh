set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/solver.pt --log_file ../output/vkitti-rf_norm-prnorm-gtseg-gtflow/log_vkitti-rf_norm-prnorm-gtseg-gtflow --blobs prnorm_in gtseg_in gtflow_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm-gtseg-gtflow/log_vkitti-rf_norm-prnorm-gtseg-gtflow

cp ../models/vkitti-rf_norm-prnorm-gtseg-gtflow/vkitti-rf_norm-prnorm-gtseg-gtflow_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/vkitti-rf_norm-prnorm-gtseg-gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm-gtseg-gtflow.yaml --proto ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/test.pt --weight ../models/vkitti-rf_norm-prnorm-gtseg-gtflow/vkitti-rf_norm-prnorm-gtseg-gtflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm-gtseg-gtflow --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/perimg.md --report ../runs/vkitti-rf_norm-prnorm-gtseg-gtflow/README.md
