set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/gdxtracted-rf_norm-prnorm-gtflow/solver.pt --log_file ../output/gdxtracted-rf_norm-prnorm-gtflow/log_gdxtracted-rf_norm-prnorm-gtflow --blobs prnorm_in gtflow_in norm_gt out-norm --vis_path ../runs/gdxtracted-rf_norm-prnorm-gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_norm-prnorm-gtflow/log_gdxtracted-rf_norm-prnorm-gtflow

cp ../models/gdxtracted-rf_norm-prnorm-gtflow/gdxtracted-rf_norm-prnorm-gtflow_iter_200000.caffemodel ../runs/gdxtracted-rf_norm-prnorm-gtflow/gdxtracted-rf_norm-prnorm-gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_norm-prnorm-gtflow.yaml --proto ../runs/gdxtracted-rf_norm-prnorm-gtflow/test.pt --weight ../models/gdxtracted-rf_norm-prnorm-gtflow/gdxtracted-rf_norm-prnorm-gtflow_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_norm-prnorm-gtflow --out_blobs out-norm --perimg ../runs/gdxtracted-rf_norm-prnorm-gtflow/perimg.md --report ../runs/gdxtracted-rf_norm-prnorm-gtflow/README.md
