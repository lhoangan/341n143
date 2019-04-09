set -x

export CUDA_VISIBLE_DEVICES=0

python train.py  --solver ../runs/vkitti-rf_seg-prseg_prflow_prnorm/solver.pt --log_file ../output/vkitti-rf_seg-prseg_prflow_prnorm/log_vkitti-rf_seg-prseg_prflow_prnorm --blobs prseg_in prflow_in prnorm_in seg_gt out-seg --vis_path ../runs/vkitti-rf_seg-prseg_prflow_prnorm --pycaffe /home/hale/caffe/segflow-caffe/python 2>&1 | tee ../output/vkitti-rf_seg-prseg_prflow_prnorm/log_vkitti-rf_seg-prseg_prflow_prnorm

cp ../models/vkitti-rf_seg-prseg_prflow_prnorm/vkitti-rf_seg-prseg_prflow_prnorm_iter_200000.caffemodel ../runs/vkitti-rf_seg-prseg_prflow_prnorm/vkitti-rf_seg-prseg_prflow_prnorm_testweight.caffemodel

python inference.py --config ../configs/general.yaml --exp ../experiments/vkitti-rf_seg-prseg_prflow_prnorm.yaml --proto ../runs/vkitti-rf_seg-prseg_prflow_prnorm/test.pt --weight ../models/vkitti-rf_seg-prseg_prflow_prnorm/vkitti-rf_seg-prseg_prflow_prnorm_iter_200000.caffemodel --outdir ../output/vkitti-rf_seg-prseg_prflow_prnorm --out_blobs out-seg --perimg ../runs/vkitti-rf_seg-prseg_prflow_prnorm/perimg.md --report ../runs/vkitti-rf_seg-prseg_prflow_prnorm/README.md
