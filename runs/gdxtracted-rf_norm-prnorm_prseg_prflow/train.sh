set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/solver.pt --log_file ../output/gdxtracted-rf_norm-prnorm_prseg_prflow/log_gdxtracted-rf_norm-prnorm_prseg_prflow --blobs prnorm_in prseg_in prflow_in norm_gt out-norm --vis_path ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_norm-prnorm_prseg_prflow/log_gdxtracted-rf_norm-prnorm_prseg_prflow

cp ../models/gdxtracted-rf_norm-prnorm_prseg_prflow/gdxtracted-rf_norm-prnorm_prseg_prflow_iter_200000.caffemodel ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/gdxtracted-rf_norm-prnorm_prseg_prflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_norm-prnorm_prseg_prflow.yaml --proto ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/test.pt --weight ../models/gdxtracted-rf_norm-prnorm_prseg_prflow/gdxtracted-rf_norm-prnorm_prseg_prflow_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_norm-prnorm_prseg_prflow --out_blobs out-norm --perimg ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/perimg.md --report ../runs/gdxtracted-rf_norm-prnorm_prseg_prflow/README.md
