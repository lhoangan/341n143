set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/gdxtracted-rf_norm-prnorm-gtseg/solver.pt --log_file ../output/gdxtracted-rf_norm-prnorm-gtseg/log_gdxtracted-rf_norm-prnorm-gtseg --blobs prnorm_in gtseg_in norm_gt out-norm --vis_path ../runs/gdxtracted-rf_norm-prnorm-gtseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_norm-prnorm-gtseg/log_gdxtracted-rf_norm-prnorm-gtseg

cp ../models/gdxtracted-rf_norm-prnorm-gtseg/gdxtracted-rf_norm-prnorm-gtseg_iter_200000.caffemodel ../runs/gdxtracted-rf_norm-prnorm-gtseg/gdxtracted-rf_norm-prnorm-gtseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_norm-prnorm-gtseg.yaml --proto ../runs/gdxtracted-rf_norm-prnorm-gtseg/test.pt --weight ../models/gdxtracted-rf_norm-prnorm-gtseg/gdxtracted-rf_norm-prnorm-gtseg_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_norm-prnorm-gtseg --out_blobs out-norm --perimg ../runs/gdxtracted-rf_norm-prnorm-gtseg/perimg.md --report ../runs/gdxtracted-rf_norm-prnorm-gtseg/README.md
