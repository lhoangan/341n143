set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_norm-prnorm-gtseg/solver.pt --log_file ../output/vkitti-rf_norm-prnorm-gtseg/log_vkitti-rf_norm-prnorm-gtseg --blobs prnorm_in gtseg_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm-gtseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm-gtseg/log_vkitti-rf_norm-prnorm-gtseg

cp ../models/vkitti-rf_norm-prnorm-gtseg/vkitti-rf_norm-prnorm-gtseg_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm-gtseg/vkitti-rf_norm-prnorm-gtseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm-gtseg.yaml --proto ../runs/vkitti-rf_norm-prnorm-gtseg/test.pt --weight ../models/vkitti-rf_norm-prnorm-gtseg/vkitti-rf_norm-prnorm-gtseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm-gtseg --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm-gtseg/perimg.md --report ../runs/vkitti-rf_norm-prnorm-gtseg/README.md
