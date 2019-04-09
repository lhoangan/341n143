set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/solver.pt --log_file ../output/vkitti-rf_seg-prseg-gtflow-gtnorm/log_vkitti-rf_seg-prseg-gtflow-gtnorm --blobs prseg_in gtflow_in gtnorm_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg-gtflow-gtnorm/log_vkitti-rf_seg-prseg-gtflow-gtnorm

cp ../models/vkitti-rf_seg-prseg-gtflow-gtnorm/vkitti-rf_seg-prseg-gtflow-gtnorm_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/vkitti-rf_seg-prseg-gtflow-gtnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg-gtflow-gtnorm.yaml --proto ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/test.pt --weight ../models/vkitti-rf_seg-prseg-gtflow-gtnorm/vkitti-rf_seg-prseg-gtflow-gtnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg-gtflow-gtnorm --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/perimg.md --report ../runs/vkitti-rf_seg-prseg-gtflow-gtnorm/README.md
