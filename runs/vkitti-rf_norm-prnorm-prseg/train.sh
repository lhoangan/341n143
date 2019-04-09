set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_norm-prnorm-prseg/solver.pt --log_file ../output/vkitti-rf_norm-prnorm-prseg/log_vkitti-rf_norm-prnorm-prseg --blobs prnorm_in prseg_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm-prseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm-prseg/log_vkitti-rf_norm-prnorm-prseg

cp ../models/vkitti-rf_norm-prnorm-prseg/vkitti-rf_norm-prnorm-prseg_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm-prseg/vkitti-rf_norm-prnorm-prseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm-prseg.yaml --proto ../runs/vkitti-rf_norm-prnorm-prseg/test.pt --weight ../models/vkitti-rf_norm-prnorm-prseg/vkitti-rf_norm-prnorm-prseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm-prseg --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm-prseg/perimg.md --report ../runs/vkitti-rf_norm-prnorm-prseg/README.md
