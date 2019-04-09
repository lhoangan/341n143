set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/gdxtracted-rf_norm-prnorm-prseg/solver.pt --log_file ../output/gdxtracted-rf_norm-prnorm-prseg/log_gdxtracted-rf_norm-prnorm-prseg --blobs prnorm_in prseg_in norm_gt out-norm --vis_path ../runs/gdxtracted-rf_norm-prnorm-prseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_norm-prnorm-prseg/log_gdxtracted-rf_norm-prnorm-prseg

cp ../models/gdxtracted-rf_norm-prnorm-prseg/gdxtracted-rf_norm-prnorm-prseg_iter_200000.caffemodel ../runs/gdxtracted-rf_norm-prnorm-prseg/gdxtracted-rf_norm-prnorm-prseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_norm-prnorm-prseg.yaml --proto ../runs/gdxtracted-rf_norm-prnorm-prseg/test.pt --weight ../models/gdxtracted-rf_norm-prnorm-prseg/gdxtracted-rf_norm-prnorm-prseg_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_norm-prnorm-prseg --out_blobs out-norm --perimg ../runs/gdxtracted-rf_norm-prnorm-prseg/perimg.md --report ../runs/gdxtracted-rf_norm-prnorm-prseg/README.md
