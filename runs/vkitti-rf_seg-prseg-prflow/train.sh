set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/vkitti-rf_seg-prseg-prflow/solver.pt --log_file ../output/vkitti-rf_seg-prseg-prflow/log_vkitti-rf_seg-prseg-prflow --blobs prseg_in prflow_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg-prflow --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg-prflow/log_vkitti-rf_seg-prseg-prflow

cp ../models/vkitti-rf_seg-prseg-prflow/vkitti-rf_seg-prseg-prflow_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg-prflow/vkitti-rf_seg-prseg-prflow_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg-prflow.yaml --proto ../runs/vkitti-rf_seg-prseg-prflow/test.pt --weight ../models/vkitti-rf_seg-prseg-prflow/vkitti-rf_seg-prseg-prflow_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg-prflow --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg-prflow/perimg.md --report ../runs/vkitti-rf_seg-prseg-prflow/README.md
