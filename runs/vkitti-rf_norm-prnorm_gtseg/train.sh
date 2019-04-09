set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_norm-prnorm_gtseg/solver.pt --log_file ../output/vkitti-rf_norm-prnorm_gtseg/log_vkitti-rf_norm-prnorm_gtseg --blobs prnorm_in gtseg_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm_gtseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm_gtseg/log_vkitti-rf_norm-prnorm_gtseg

cp ../models/vkitti-rf_norm-prnorm_gtseg/vkitti-rf_norm-prnorm_gtseg_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm_gtseg/vkitti-rf_norm-prnorm_gtseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm_gtseg.yaml --proto ../runs/vkitti-rf_norm-prnorm_gtseg/test.pt --weight ../models/vkitti-rf_norm-prnorm_gtseg/vkitti-rf_norm-prnorm_gtseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm_gtseg --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm_gtseg/perimg.md --report ../runs/vkitti-rf_norm-prnorm_gtseg/README.md
