set -x

export CUDA_VISIBLE_DEVICES=2

python train.py  --solver ../runs/vkitti-rf_seg-prseg-gtflow/solver.pt --log_file ../output/vkitti-rf_seg-prseg-gtflow/log_vkitti-rf_seg-prseg-gtflow --blobs prseg_in gtflow_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg-gtflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg-gtflow/log_vkitti-rf_seg-prseg-gtflow

cp ../models/vkitti-rf_seg-prseg-gtflow/vkitti-rf_seg-prseg-gtflow_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg-gtflow/vkitti-rf_seg-prseg-gtflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg-gtflow.yaml --proto ../runs/vkitti-rf_seg-prseg-gtflow/test.pt --weight ../models/vkitti-rf_seg-prseg-gtflow/vkitti-rf_seg-prseg-gtflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg-gtflow --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg-gtflow/perimg.md --report ../runs/vkitti-rf_seg-prseg-gtflow/README.md
