set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_norm-prnorm_prseg/solver.pt --log_file ../output/vkitti-rf_norm-prnorm_prseg/log_vkitti-rf_norm-prnorm_prseg --blobs prnorm_in prseg_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm_prseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm_prseg/log_vkitti-rf_norm-prnorm_prseg

cp ../models/vkitti-rf_norm-prnorm_prseg/vkitti-rf_norm-prnorm_prseg_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm_prseg/vkitti-rf_norm-prnorm_prseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm_prseg.yaml --proto ../runs/vkitti-rf_norm-prnorm_prseg/test.pt --weight ../models/vkitti-rf_norm-prnorm_prseg/vkitti-rf_norm-prnorm_prseg_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm_prseg --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm_prseg/perimg.md --report ../runs/vkitti-rf_norm-prnorm_prseg/README.md
