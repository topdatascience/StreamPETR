#!/bin/bash

# Assign arguments to variables
ROOT_PATH="data/nuscenes"
VERSION="v1.0-mini"
EXTRA_TAG="nuscenes2d"
MAX_SWEEPS=10

# Navigate to the ROS 2 workspace
cd /root/ros2_ws

# Source the ROS 2 setup file
source install/local_setup.bash

cd /root

# Run the ROS 2 launch file
ros2 launch streampetr_ros create_nuscenes_launch.py root_path:=$ROOT_PATH version:=$VERSION extra_tag:=$EXTRA_TAG max_sweeps:=$MAX_SWEEPS

