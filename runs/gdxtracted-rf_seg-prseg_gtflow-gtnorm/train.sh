set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/solver.pt --log_file ../output/gdxtracted-rf_seg-prseg_gtflow-gtnorm/log_gdxtracted-rf_seg-prseg_gtflow-gtnorm --blobs prseg_in gtflow_in gtnorm_in seg_gt out-seg --vis_path ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_seg-prseg_gtflow-gtnorm/log_gdxtracted-rf_seg-prseg_gtflow-gtnorm

cp ../models/gdxtracted-rf_seg-prseg_gtflow-gtnorm/gdxtracted-rf_seg-prseg_gtflow-gtnorm_iter_200000.caffemodel ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/gdxtracted-rf_seg-prseg_gtflow-gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_seg-prseg_gtflow-gtnorm.yaml --proto ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/test.pt --weight ../models/gdxtracted-rf_seg-prseg_gtflow-gtnorm/gdxtracted-rf_seg-prseg_gtflow-gtnorm_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_seg-prseg_gtflow-gtnorm --out_blobs out-seg --perimg ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/perimg.md --report ../runs/gdxtracted-rf_seg-prseg_gtflow-gtnorm/README.md
