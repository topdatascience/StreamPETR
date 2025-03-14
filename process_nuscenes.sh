#!/bin/bash

# Assign arguments to variables
CONFIG_PATH=/usr/local/lib/python3.8/dist-packages/projects/configs/RepDETR3D/repdetr3d_eva02_800_bs2_seq_24e.py
CHECKPOINT_PATH=models/repdetr3d_eva02_800_bs2_seq_24e.pth
OUTPUT_DIRECTORY=result

# Navigate to the ROS 2 workspace
cd /root/ros2_ws

# Source the ROS 2 setup file
source install/local_setup.bash

cd /root

# Run the ROS 2 launch file
ros2 launch streampetr_ros repdetr3d_launch.py config_path:=$CONFIG_PATH checkpoint_path:=$CHECKPOINT_PATH output_directory:=$OUTPUT_DIRECTORY

