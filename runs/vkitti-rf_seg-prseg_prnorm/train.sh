set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/vkitti-rf_seg-prseg_prnorm/solver.pt --log_file ../output/vkitti-rf_seg-prseg_prnorm/log_vkitti-rf_seg-prseg_prnorm --blobs prseg_in prnorm_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg_prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg_prnorm/log_vkitti-rf_seg-prseg_prnorm

cp ../models/vkitti-rf_seg-prseg_prnorm/vkitti-rf_seg-prseg_prnorm_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg_prnorm/vkitti-rf_seg-prseg_prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg_prnorm.yaml --proto ../runs/vkitti-rf_seg-prseg_prnorm/test.pt --weight ../models/vkitti-rf_seg-prseg_prnorm/vkitti-rf_seg-prseg_prnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg_prnorm --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg_prnorm/perimg.md --report ../runs/vkitti-rf_seg-prseg_prnorm/README.md
