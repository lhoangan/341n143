set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/gdxtracted-rf_seg-prseg-prnorm/solver.pt --log_file ../output/gdxtracted-rf_seg-prseg-prnorm/log_gdxtracted-rf_seg-prseg-prnorm --blobs prseg_in prnorm_in seg_gt out-seg --vis_path ../runs/gdxtracted-rf_seg-prseg-prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_seg-prseg-prnorm/log_gdxtracted-rf_seg-prseg-prnorm

cp ../models/gdxtracted-rf_seg-prseg-prnorm/gdxtracted-rf_seg-prseg-prnorm_iter_200000.caffemodel ../runs/gdxtracted-rf_seg-prseg-prnorm/gdxtracted-rf_seg-prseg-prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_seg-prseg-prnorm.yaml --proto ../runs/gdxtracted-rf_seg-prseg-prnorm/test.pt --weight ../models/gdxtracted-rf_seg-prseg-prnorm/gdxtracted-rf_seg-prseg-prnorm_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_seg-prseg-prnorm --out_blobs out-seg --perimg ../runs/gdxtracted-rf_seg-prseg-prnorm/perimg.md --report ../runs/gdxtracted-rf_seg-prseg-prnorm/README.md
