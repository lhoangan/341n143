set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/solver.pt --log_file ../output/gdxtracted-rf_norm-prnorm_gtseg_gtflow/log_gdxtracted-rf_norm-prnorm_gtseg_gtflow --blobs prnorm_in gtseg_in gtflow_in norm_gt out-norm --vis_path ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_norm-prnorm_gtseg_gtflow/log_gdxtracted-rf_norm-prnorm_gtseg_gtflow

cp ../models/gdxtracted-rf_norm-prnorm_gtseg_gtflow/gdxtracted-rf_norm-prnorm_gtseg_gtflow_iter_200000.caffemodel ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/gdxtracted-rf_norm-prnorm_gtseg_gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_norm-prnorm_gtseg_gtflow.yaml --proto ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/test.pt --weight ../models/gdxtracted-rf_norm-prnorm_gtseg_gtflow/gdxtracted-rf_norm-prnorm_gtseg_gtflow_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_norm-prnorm_gtseg_gtflow --out_blobs out-norm --perimg ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/perimg.md --report ../runs/gdxtracted-rf_norm-prnorm_gtseg_gtflow/README.md
