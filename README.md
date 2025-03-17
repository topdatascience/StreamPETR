<div align="center">
<h1>StreamPETR</h1>
<h3>[ICCV2023] Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection</h3>
</div>

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/exploring-object-centric-temporal-modeling/3d-multi-object-tracking-on-nuscenes-camera-1)](https://paperswithcode.com/sota/3d-multi-object-tracking-on-nuscenes-camera-1?p=exploring-object-centric-temporal-modeling)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/exploring-object-centric-temporal-modeling/3d-object-detection-on-nuscenes-camera-only)](https://paperswithcode.com/sota/3d-object-detection-on-nuscenes-camera-only?p=exploring-object-centric-temporal-modeling)
[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2303.11926)

<div align="center">
  <img src="figs/framework.png" width="800"/>
</div><br/>

## Docker and ROS Integration

We have included Docker files and a bash script to streamline the setup and execution of ROS processes.

### Docker Setup

To build the Docker image, navigate to the root directory of the repository and run:
```bash
docker compose -f docker-compose.yml build
```

To run the Docker container:
```bash
docker compose -f docker-compose.yml up
```

### For external users

For non-TDS members, please use the following token to login docker. This token has limited access to TDS github; and will expire in 3 months.

```
GITHUB_TOKEN="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"
echo $GITHUB_TOKEN | docker login ghcr.io -u tds-dt --password-stdin

docker compose -f docker-compose.yml pull
docker compose -f docker-compose.yml up
```

### Why Docker?

Foxy is the ROS distribution(EOL) built for and supports python3.8. The codespace strictly assumes this version of python and the libraries are creating so many conflicts. You can save your time without having to install the depedencies yourself.

## Dataset & Config Instructions

This repository currently focuses on only NuScenes dataset structure. Please first download NuScenes v1.0-mini version from [nuscenes](https://www.nuscenes.org/nuscenes#download) and extract it to the `data/nuscenes` folder. Please also download the model by using `download.sh` in the `models`folder.

### Bash Scripts for NuScenes Dataset

There are several bash scripts provided to help you manage the NuScenes dataset:

#### create_nuscenes.sh

This script is used to create the necessary directory structure for the NuScenes dataset and download the required files. After you run this command, you should see `nuscenes2d_temporal_infos_val.pkl` and `nuscenes2d_temporal_infos_train.pk` in the `data/nuscenes` folder.

#### process_nuscenes.sh

This script processes the exported data, e.g. `nuscenes2d_temporal_infos_val.pkl`, and runs the inference using the model. If it runs successfully, you will see a json file in a directory similar to `result/repdetr3d_eva02_800_bs2_seq_24e/Fri_Mar_14_12_12_55_2025/pts_bbox/results_nusc.json`.

#### visualize_nuscenes.sh

This script provides visualization tools to help you inspect the NuScenes dataset and verify the correctness of the data processing steps.

To use these scripts, edit `docker-compose.yml` entry command and run them as follows:
```bash
bash create_nuscenes.sh
bash process_nuscenes.sh
bash visualize_nuscenes.sh --result_json result/../../results_nusc
```

### Custom Config

In this repository, the model was chosen according to the mAP score on the nuscenes validation dataset. If you want to use your own dataset, it'd be easier to convert your dataset into nuscenes format first as the dataset builder will fetch and consume extrinsic parameters while preparing the items. Please take a look at `projects/configs/RepDETR3D/repdetr3d_eva02_800_bs2_seq_24e.py` to see `point_cloud_range`, `voxel_size`, and `data_root`. 

## Introduction

This repository is an official implementation of StreamPETR.

## News
- [2023/07/14] StreamPETR is accepted by ICCV 2023.
- [2023/05/03] StreamPETR-Large is the first online multi-view method that achieves comparable performance (62.0 mAP, 67.6 NDS and 65.3 AMOTA) with the baseline of lidar-based method. 

## Getting Started

Please follow our documentation step by step. If you like our work, please recommend it to your colleagues and friends.

1. [**Environment Setup.**](./docs/setup.md)
2. [**Data Preparation.**](./docs/data_preparation.md)
3. [**Training and Inference.**](./docs/training_inference.md)

## Model Zoo
<div align="center">
  <img src="figs/fps.png" width="550"/>
</div><br/>

## Results on NuScenes Val Set.
| Model | Setting |Pretrain| Lr Schd | Training Time | NDS| mAP|FPS-pytorch | Config | Download |
| :---: | :---: | :---: | :---: | :---:|:---:| :---: | :---: | :---: | :---: |
RepDETR3D| EVA02-L - 900q | [EVA02-L](https://github.com/exiawsh/storage/releases/download/v1.0/eva02_L_coco_det_sys_o365_remapped.pth) | 24ep | 12 hours (A100) | 60.8 | 52.1 | - |[config](projects/configs/RepDETR3D/repdetr3d_eva02_800_bs2_seq_24e.py) |[model](https://github.com/exiawsh/storage/releases/download/v1.0/repdetr3d_eva02_800_bs2_seq_24e.pth)|
|StreamPETR| V2-99 - 900q | [FCOS3D](https://github.com/exiawsh/storage/releases/download/v1.0/fcos3d_vovnet_imgbackbone-remapped.pth) | 24ep | 13 hours | 57.1 | 48.2 | 12.5 |[config](projects/configs/StreamPETR/stream_petr_vov_flash_800_bs2_seq_24e.py) |[model](https://github.com/exiawsh/storage/releases/download/v1.0/stream_petr_vov_flash_800_bs2_seq_24e.pth)/[log](https://github.com/exiawsh/storage/releases/download/v1.0/stream_petr_vov_flash_800_bs2_seq_24e.log) |
RepDETR3D| V2-99 - 900q | [FCOS3D](https://github.com/exiawsh/storage/releases/download/v1.0/fcos3d_vovnet_imgbackbone-remapped.pth) | 24ep | 13 hours | 58.4 | 50.1 | 13.1 |[config](projects/configs/RepDETR3D/repdetr3d_vov_800_bs2_seq_24e.py) |[model](https://github.com/exiawsh/storage/releases/download/v1.0/repdetr3d_vov_800_bs2_seq_24e.pth)/[log](https://github.com/exiawsh/storage/releases/download/v1.0/repdetr3d_vov_800_bs2_seq_24e.log) |
|StreamPETR| R50 - 900q | ImageNet | 90ep | 36 hours | 53.7 | 43.2 | 26.7 |[config](projects/configs/StreamPETR/stream_petr_r50_flash_704_bs2_seq_90e.py) |[model](https://github.com/exiawsh/storage/releases/download/v1.0/stream_petr_r50_flash_704_bs2_seq_90e.pth)/[log](https://github.com/exiawsh/storage/releases/download/v1.0/stream_petr_r50_flash_704_bs2_seq_90e.log) |
|StreamPETR| R50 - 428q | [NuImg](https://download.openmmlab.com/mmdetection3d/v0.1.0_models/nuimages_semseg/cascade_mask_rcnn_r50_fpn_coco-20e_20e_nuim/cascade_mask_rcnn_r50_fpn_coco-20e_20e_nuim_20201009_124951-40963960.pth) | 60ep | 26 hours | 54.6 |44.9 | 31.7 |[config](projects/configs/StreamPETR/stream_petr_r50_flash_704_bs2_seq_428q_nui_60e.py)| [model](https://github.com/exiawsh/storage/releases/download/v1.0/stream_petr_r50_flash_704_bs2_seq_428q_nui_60e.pth)/[log](https://github.com/exiawsh/storage/releases/download/v1.0/stream_petr_r50_flash_704_bs2_seq_428q_nui_60e.log) |


The detailed results can be found in the training log. For other results on nuScenes val set, please see [Here](docs/training_inference.md).
**Notes**: 
- FPS is measured on NVIDIA RTX 3090 GPU with batch size of 1 (containing 6 view images, without using flash attention) and FP32. 
- The training time is measured with 8x 2080ti GPUs.
- RepDETR3D uses deformable attention, which is inspired by DETR3D and Sparse4D.

## Results on NuScenes Test Set.
| Model | Setting |Pretrain|NDS| mAP|AMOTA|AMOTP|
| :---: | :---: | :---: | :---: | :---:| :---: | :---:|
|StreamPETR| V2-99 - 900q | [DD3D](https://github.com/exiawsh/storage/releases/download/v1.0/dd3d_det_final.pth) | 63.6| 55.0 | - | - |
|StreamPETR| ViT-Large-900q | - | 67.6| 62.0 | 65.3| 87.6 |


## Currently Supported Features

- [x] StreamPETR code (also including PETR and Focal-PETR)
- [x] Flash attention
- [x] Deformable attention (RepDETR3D)
- [x] Checkpoints
- [x] Sliding window training
- [x] Efficient training in streaming video
- [x] [TensorRT inference](https://github.com/NVIDIA/DL4AGX/tree/master/AV-Solutions/streampetr-trt)
- [x] 3D object tracking

## Acknowledgements

We thank these great works and open-source codebases:

* 3D Detection. [MMDetection3d](https://github.com/open-mmlab/mmdetection3d), [DETR3D](https://github.com/WangYueFt/detr3d), [PETR](https://github.com/megvii-research/PETR), [BEVFormer](https://github.com/fundamentalvision/BEVFormer), [SOLOFusion](https://github.com/Divadi/SOLOFusion), [Sparse4D](https://github.com/linxuewu/Sparse4D).
* Multi-object tracking. [MOTR](https://github.com/megvii-research/MOTR), [PF-Track](https://github.com/TRI-ML/PF-Track).


## Citation

If you find StreamPETR is useful in your research or applications, please consider giving us a star 🌟 and citing it by the following BibTeX entry.
```bibtex
@article{wang2023exploring,
  title={Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection},
  author={Wang, Shihao and Liu, Yingfei and Wang, Tiancai and Li, Ying and Zhang, Xiangyu},
  journal={arXiv preprint arXiv:2303.11926},
  year={2023}
}
```
