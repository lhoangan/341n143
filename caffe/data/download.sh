#!/bin/bash 

mkdir FlyingThings3D_release
cd FlyingThings3D_release

wget http://lmb.informatik.uni-freiburg.de/data/SceneFlowDatasets_CVPR16/Release_april16/data/FlyingThings3D/raw_data/flyingthings3d__frames_cleanpass.tar
wget http://lmb.informatik.uni-freiburg.de/data/SceneFlowDatasets_CVPR16/Release_april16/data/FlyingThings3D/derived_data/flyingthings3d__disparity.tar.bz2

tar xvf flyingthings3d__frames_cleanpass.tar
tar xvf flyingthings3d__disparity.tar.bz2

cd .. 
wget http://lmb.informatik.uni-freiburg.de/resources/datasets/FlyingChairs/FlyingChairs.zip
unzip FlyingChairs.zip
