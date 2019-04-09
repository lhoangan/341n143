set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/gdxtracted-rf_seg-prseg_gtflow/solver.pt --log_file ../output/gdxtracted-rf_seg-prseg_gtflow/log_gdxtracted-rf_seg-prseg_gtflow --blobs prseg_in gtflow_in seg_gt out-seg --vis_path ../runs/gdxtracted-rf_seg-prseg_gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_seg-prseg_gtflow/log_gdxtracted-rf_seg-prseg_gtflow

cp ../models/gdxtracted-rf_seg-prseg_gtflow/gdxtracted-rf_seg-prseg_gtflow_iter_200000.caffemodel ../runs/gdxtracted-rf_seg-prseg_gtflow/gdxtracted-rf_seg-prseg_gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_seg-prseg_gtflow.yaml --proto ../runs/gdxtracted-rf_seg-prseg_gtflow/test.pt --weight ../models/gdxtracted-rf_seg-prseg_gtflow/gdxtracted-rf_seg-prseg_gtflow_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_seg-prseg_gtflow --out_blobs out-seg --perimg ../runs/gdxtracted-rf_seg-prseg_gtflow/perimg.md --report ../runs/gdxtracted-rf_seg-prseg_gtflow/README.md
