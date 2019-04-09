set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/gdxtracted-rf_norm-prnorm_gtseg/solver.pt --log_file ../output/gdxtracted-rf_norm-prnorm_gtseg/log_gdxtracted-rf_norm-prnorm_gtseg --blobs prnorm_in gtseg_in norm_gt out-norm --vis_path ../runs/gdxtracted-rf_norm-prnorm_gtseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_norm-prnorm_gtseg/log_gdxtracted-rf_norm-prnorm_gtseg

cp ../models/gdxtracted-rf_norm-prnorm_gtseg/gdxtracted-rf_norm-prnorm_gtseg_iter_200000.caffemodel ../runs/gdxtracted-rf_norm-prnorm_gtseg/gdxtracted-rf_norm-prnorm_gtseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_norm-prnorm_gtseg.yaml --proto ../runs/gdxtracted-rf_norm-prnorm_gtseg/test.pt --weight ../models/gdxtracted-rf_norm-prnorm_gtseg/gdxtracted-rf_norm-prnorm_gtseg_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_norm-prnorm_gtseg --out_blobs out-norm --perimg ../runs/gdxtracted-rf_norm-prnorm_gtseg/perimg.md --report ../runs/gdxtracted-rf_norm-prnorm_gtseg/README.md
