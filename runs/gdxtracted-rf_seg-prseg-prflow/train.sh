set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/gdxtracted-rf_seg-prseg-prflow/solver.pt --log_file ../output/gdxtracted-rf_seg-prseg-prflow/log_gdxtracted-rf_seg-prseg-prflow --blobs prseg_in prflow_in seg_gt out-seg --vis_path ../runs/gdxtracted-rf_seg-prseg-prflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/gdxtracted-rf_seg-prseg-prflow/log_gdxtracted-rf_seg-prseg-prflow

cp ../models/gdxtracted-rf_seg-prseg-prflow/gdxtracted-rf_seg-prseg-prflow_iter_200000.caffemodel ../runs/gdxtracted-rf_seg-prseg-prflow/gdxtracted-rf_seg-prseg-prflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/gdxtracted-rf_seg-prseg-prflow.yaml --proto ../runs/gdxtracted-rf_seg-prseg-prflow/test.pt --weight ../models/gdxtracted-rf_seg-prseg-prflow/gdxtracted-rf_seg-prseg-prflow_iter_200000.caffemodel --outdir ../output/gdxtracted-rf_seg-prseg-prflow --out_blobs out-seg --perimg ../runs/gdxtracted-rf_seg-prseg-prflow/perimg.md --report ../runs/gdxtracted-rf_seg-prseg-prflow/README.md
