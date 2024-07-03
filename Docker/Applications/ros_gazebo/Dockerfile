# Use the official ROS base image
FROM osrf/ros:noetic-desktop-full

# Install Gazebo and GUI dependencies
RUN apt-get update && apt-get install -y \
    gazebo11 \
    ros-noetic-gazebo-ros-pkgs \
    ros-noetic-gazebo-ros-control \
    libgl1-mesa-glx \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libxrandr2 \
    mesa-utils \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set up environment
ENV ROS_DISTRO noetic

# Source ROS setup.bash
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Set the working directory
WORKDIR /root

# Expose necessary ports
EXPOSE 11311

# Entry point
ENTRYPOINT ["bash"]
