set -x

export CUDA_VISIBLE_DEVICES=1

python train.py  --solver ../runs/vkitti-rf_seg-prseg-prnorm/solver.pt --log_file ../output/vkitti-rf_seg-prseg-prnorm/log_vkitti-rf_seg-prseg-prnorm --blobs prseg_in prnorm_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg-prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg-prnorm/log_vkitti-rf_seg-prseg-prnorm

cp ../models/vkitti-rf_seg-prseg-prnorm/vkitti-rf_seg-prseg-prnorm_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg-prnorm/vkitti-rf_seg-prseg-prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg-prnorm.yaml --proto ../runs/vkitti-rf_seg-prseg-prnorm/test.pt --weight ../models/vkitti-rf_seg-prseg-prnorm/vkitti-rf_seg-prseg-prnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg-prnorm --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg-prnorm/perimg.md --report ../runs/vkitti-rf_seg-prseg-prnorm/README.md
