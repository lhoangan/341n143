set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/gdxtracted-rf_seg-prseg_prflow/solver.pt --log_file ../output/gdxtracted-rf_seg-prseg_prflow/log_gdxtracted-rf_seg-prseg_prflow --blobs prseg_in prflow_in seg_gt out-seg --vis_path ../runs/gdxtracted-rf_seg-prseg_prflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_seg-prseg_prflow/log_gdxtracted-rf_seg-prseg_prflow

cp ../models/gdxtracted-rf_seg-prseg_prflow/gdxtracted-rf_seg-prseg_prflow_iter_200000.caffemodel ../runs/gdxtracted-rf_seg-prseg_prflow/gdxtracted-rf_seg-prseg_prflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_seg-prseg_prflow.yaml --proto ../runs/gdxtracted-rf_seg-prseg_prflow/test.pt --weight ../models/gdxtracted-rf_seg-prseg_prflow/gdxtracted-rf_seg-prseg_prflow_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_seg-prseg_prflow --out_blobs out-seg --perimg ../runs/gdxtracted-rf_seg-prseg_prflow/perimg.md --report ../runs/gdxtracted-rf_seg-prseg_prflow/README.md
