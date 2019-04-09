set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/gdxtracted-rf_norm-prnorm_prseg/solver.pt --log_file ../output/gdxtracted-rf_norm-prnorm_prseg/log_gdxtracted-rf_norm-prnorm_prseg --blobs prnorm_in prseg_in norm_gt out-norm --vis_path ../runs/gdxtracted-rf_norm-prnorm_prseg --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_norm-prnorm_prseg/log_gdxtracted-rf_norm-prnorm_prseg

cp ../models/gdxtracted-rf_norm-prnorm_prseg/gdxtracted-rf_norm-prnorm_prseg_iter_200000.caffemodel ../runs/gdxtracted-rf_norm-prnorm_prseg/gdxtracted-rf_norm-prnorm_prseg_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_norm-prnorm_prseg.yaml --proto ../runs/gdxtracted-rf_norm-prnorm_prseg/test.pt --weight ../models/gdxtracted-rf_norm-prnorm_prseg/gdxtracted-rf_norm-prnorm_prseg_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_norm-prnorm_prseg --out_blobs out-norm --perimg ../runs/gdxtracted-rf_norm-prnorm_prseg/perimg.md --report ../runs/gdxtracted-rf_norm-prnorm_prseg/README.md
