set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/vkitti-rf_norm-prnorm_gtflow/solver.pt --log_file ../output/vkitti-rf_norm-prnorm_gtflow/log_vkitti-rf_norm-prnorm_gtflow --blobs prnorm_in gtflow_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm_gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm_gtflow/log_vkitti-rf_norm-prnorm_gtflow

cp ../models/vkitti-rf_norm-prnorm_gtflow/vkitti-rf_norm-prnorm_gtflow_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm_gtflow/vkitti-rf_norm-prnorm_gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm_gtflow.yaml --proto ../runs/vkitti-rf_norm-prnorm_gtflow/test.pt --weight ../models/vkitti-rf_norm-prnorm_gtflow/vkitti-rf_norm-prnorm_gtflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm_gtflow --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm_gtflow/perimg.md --report ../runs/vkitti-rf_norm-prnorm_gtflow/README.md
