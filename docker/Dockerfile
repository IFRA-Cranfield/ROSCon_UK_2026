# ROSCon UK 2026: ROS 2 Humble with Gazebo Classic.

# Build from the repository root:
# docker build -f docker/Dockerfile -t rosconuk26:humble .
FROM osrf/ros:humble-desktop-full

# Environment variables:
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=humble
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ENV ALSOFT_DRIVERS=null

# ============================================================== #
# Core development tools and ROS 2 Humble dependencies:
# ============================================================== #

# Development tools:
RUN apt-get update && apt-get install -y \
    git \
    ros-dev-tools \
    ros-humble-xacro \
    ros-humble-rmw-cyclonedds-cpp \
    && rm -rf /var/lib/apt/lists/*

# ROS 2 Control:
RUN apt-get update && apt-get install -y \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-gripper-controllers \
    && rm -rf /var/lib/apt/lists/*

# MoveIt 2:
RUN apt-get update && apt-get install -y \
    ros-humble-moveit \
    && rm -rf /var/lib/apt/lists/*

# Gazebo Simulator:
RUN apt-get update && apt-get install -y \
    gazebo \
    ros-humble-gazebo-ros2-control \
    ros-humble-gazebo-ros-pkgs \
    && rm -rf /var/lib/apt/lists/*

# ============================================================== #
# Workspace:
# ============================================================== #

WORKDIR /dev_ws
RUN mkdir -p /dev_ws/src && \
    ln -s /dev_ws /root/dev_ws

# ============================================================== #
# gazebo_ros2_control 0.4.6 workaround:
# ============================================================== #

RUN apt-get update && \
    apt-get remove -y ros-humble-gazebo-ros2-control && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /dev_ws/src

RUN git clone https://github.com/ros-controls/gazebo_ros2_control.git && \
    cd gazebo_ros2_control && \
    git reset --hard 9a3736c

# ============================================================== #
# ROBOT DRIVERS:
# ============================================================== #

# ABB:
RUN mkdir -p /dev_ws/src/ABBDriver
WORKDIR /dev_ws/src/ABBDriver
RUN git clone https://github.com/PickNikRobotics/abb_ros2.git -b rolling
RUN vcs import < abb_ros2/abb.repos

RUN rosdep update && \
    apt-get update && \
    rosdep install \
        -r \
        --from-paths /dev_ws/src \
        --ignore-src \
        --rosdistro humble \
        -y && \
    rm -rf /var/lib/apt/lists/*

# UNIVERSAL ROBOTS:
RUN apt-get update && apt-get install -y \
    ros-humble-ur \
    && rm -rf /var/lib/apt/lists/*

# ============================================================== #
# ROSCon UK 2026 workspace sources and ros2srrc dependencies:
# ============================================================== #

WORKDIR /dev_ws/src

RUN git clone -b humble https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl.git

RUN git clone -b humble https://github.com/IFRA-Cranfield/IFRA_LinkAttacher.git
RUN git clone -b humble https://github.com/IFRA-Cranfield/IFRA_ObjectPose.git
RUN git clone -b humble https://github.com/IFRA-Cranfield/IFRA_LinkPose.git
RUN git clone -b humble https://github.com/IFRA-Cranfield/ros2_RobotiqGripper.git

RUN git clone -b humble https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics.git
RUN git clone -b humble https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics.git

# Include the local workshop checkout from the Docker build context.
COPY . /dev_ws/src/ROSCon_UK_2026/

# ============================================================== #
# Build dependencies and workspace:
# ============================================================== #

# Small step required -> Add the move_group_interface_improved.h file:
RUN cp \
    /dev_ws/src/ros2_SimRealRobotControl/include/move_group_interface_improved.h \
    /opt/ros/humble/include/moveit/move_group_interface/move_group_interface_improved.h

# ============================================================== #
# BUILD WORKSPACE:
# ============================================================== #

WORKDIR /dev_ws
RUN /bin/bash -c \
    "source /opt/ros/humble/setup.bash && \
     colcon build"

# ============================================================== #
# Workshop perception: OpenCV, ROS image conversion and YOLO:
# ============================================================== #

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-humble-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir \
    "numpy<2" \
    opencv-contrib-python \
    ultralytics

# ============================================================== #
# Runtime shell:
# ============================================================== #

RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc && \
    echo "[ -f /dev_ws/install/local_setup.bash ] && source /dev_ws/install/local_setup.bash" >> /root/.bashrc && \
    echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> /root/.bashrc

CMD ["bash"]
