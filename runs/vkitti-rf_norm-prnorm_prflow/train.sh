set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/vkitti-rf_norm-prnorm_prflow/solver.pt --log_file ../output/vkitti-rf_norm-prnorm_prflow/log_vkitti-rf_norm-prnorm_prflow --blobs prnorm_in prflow_in norm_gt out-norm --vis_path ../runs/vkitti-rf_norm-prnorm_prflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_norm-prnorm_prflow/log_vkitti-rf_norm-prnorm_prflow

cp ../models/vkitti-rf_norm-prnorm_prflow/vkitti-rf_norm-prnorm_prflow_iter_200000.caffemodel ../runs/vkitti-rf_norm-prnorm_prflow/vkitti-rf_norm-prnorm_prflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_norm-prnorm_prflow.yaml --proto ../runs/vkitti-rf_norm-prnorm_prflow/test.pt --weight ../models/vkitti-rf_norm-prnorm_prflow/vkitti-rf_norm-prnorm_prflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_norm-prnorm_prflow --out_blobs out-norm --perimg ../runs/vkitti-rf_norm-prnorm_prflow/perimg.md --report ../runs/vkitti-rf_norm-prnorm_prflow/README.md
