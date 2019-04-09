set -x

export CUDA_VISIBLE_DEVICES=3

python train.py  --solver ../runs/vkitti-rf_seg-prseg-prflow-prnorm/solver.pt --log_file ../output/vkitti-rf_seg-prseg-prflow-prnorm/log_vkitti-rf_seg-prseg-prflow-prnorm --blobs prseg_in prflow_in prnorm_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg-prflow-prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg-prflow-prnorm/log_vkitti-rf_seg-prseg-prflow-prnorm

cp ../models/vkitti-rf_seg-prseg-prflow-prnorm/vkitti-rf_seg-prseg-prflow-prnorm_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg-prflow-prnorm/vkitti-rf_seg-prseg-prflow-prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg-prflow-prnorm.yaml --proto ../runs/vkitti-rf_seg-prseg-prflow-prnorm/test.pt --weight ../models/vkitti-rf_seg-prseg-prflow-prnorm/vkitti-rf_seg-prseg-prflow-prnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg-prflow-prnorm --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg-prflow-prnorm/perimg.md --report ../runs/vkitti-rf_seg-prseg-prflow-prnorm/README.md
