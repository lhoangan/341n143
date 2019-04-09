set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/gdxtracted-rf_seg-prseg-gtflow_gtnorm/solver.pt --log_file ../output/gdxtracted-rf_seg-prseg-gtflow_gtnorm/log_gdxtracted-rf_seg-prseg-gtflow_gtnorm --blobs prseg_in gtflow_in gtnorm_in seg_gt out-seg --vis_path ../runs/gdxtracted-rf_seg-prseg-gtflow_gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_seg-prseg-gtflow_gtnorm/log_gdxtracted-rf_seg-prseg-gtflow_gtnorm

cp ../models/gdxtracted-rf_seg-prseg-gtflow_gtnorm/gdxtracted-rf_seg-prseg-gtflow_gtnorm_iter_200000.caffemodel ../runs/gdxtracted-rf_seg-prseg-gtflow_gtnorm/gdxtracted-rf_seg-prseg-gtflow_gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_seg-prseg-gtflow_gtnorm.yaml --proto ../runs/gdxtracted-rf_seg-prseg-gtflow_gtnorm/test.pt --weight ../models/gdxtracted-rf_seg-prseg-gtflow_gtnorm/gdxtracted-rf_seg-prseg-gtflow_gtnorm_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_seg-prseg-gtflow_gtnorm --out_blobs out-seg --perimg ../runs/gdxtracted-rf_seg-prseg-gtflow_gtnorm/perimg.md --report ../runs/gdxtracted-rf_seg-prseg-gtflow_gtnorm/README.md
