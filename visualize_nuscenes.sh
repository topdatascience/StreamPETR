#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <result_json>"
    exit 1
fi

# Assign the positional argument to a variable
RESULT_JSON=$1
# Assign arguments to variables
OUT_DIR="result_vis"
DATA_ROOT="data/nuscenes"
VERSION="v1.0-mini"
USE_GT=false

# Navigate to the ROS 2 workspace
cd /root/ros2_ws

# Source the ROS 2 setup file
source install/local_setup.bash

cd /root

# Run the ROS 2 launch file
ros2 launch streampetr_ros visualize_launch.py out_dir:=$OUT_DIR result_json:=$RESULT_JSON dataroot:=$DATA_ROOT version:=$VERSION use_gt:=$USE_GT
