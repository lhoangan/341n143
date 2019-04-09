set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/vkitti-rf_seg-prseg_gtflow/solver.pt --log_file ../output/vkitti-rf_seg-prseg_gtflow/log_vkitti-rf_seg-prseg_gtflow --blobs prseg_in gtflow_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg_gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg_gtflow/log_vkitti-rf_seg-prseg_gtflow

cp ../models/vkitti-rf_seg-prseg_gtflow/vkitti-rf_seg-prseg_gtflow_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg_gtflow/vkitti-rf_seg-prseg_gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg_gtflow.yaml --proto ../runs/vkitti-rf_seg-prseg_gtflow/test.pt --weight ../models/vkitti-rf_seg-prseg_gtflow/vkitti-rf_seg-prseg_gtflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg_gtflow --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg_gtflow/perimg.md --report ../runs/vkitti-rf_seg-prseg_gtflow/README.md
