set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/solver.pt --log_file ../output/vkitti-rf_norm-prnorm_gtseg_gtflow/log_vkitti-rf_norm-prnorm_gtseg_gtflow --blobs prnorm_in gtseg_in gtflow_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm_gtseg_gtflow/log_vkitti-rf_norm-prnorm_gtseg_gtflow

cp ../models/vkitti-rf_norm-prnorm_gtseg_gtflow/vkitti-rf_norm-prnorm_gtseg_gtflow_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/vkitti-rf_norm-prnorm_gtseg_gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm_gtseg_gtflow.yaml --proto ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/test.pt --weight ../models/vkitti-rf_norm-prnorm_gtseg_gtflow/vkitti-rf_norm-prnorm_gtseg_gtflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm_gtseg_gtflow --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/perimg.md --report ../runs/vkitti-rf_norm-prnorm_gtseg_gtflow/README.md
