# ROSCon UK 2026: ROS 2 Jazzy with Gazebo Harmonic.

# Build from the repository root:
# docker build -f docker/Dockerfile -t rosconuk26:jazzy .
FROM osrf/ros:jazzy-desktop-full

# Environment variables:
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=jazzy
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
ENV ALSOFT_DRIVERS=null

# ============================================================== #
# Core development tools and ROS 2 Jazzy dependencies:
# ============================================================== #

# Development tools:
RUN apt-get update && apt-get install -y \
    git \
    ros-dev-tools \
    ros-jazzy-xacro \
    ros-jazzy-rmw-cyclonedds-cpp \
    && rm -rf /var/lib/apt/lists/*

# ROS 2 Control:
RUN apt-get update && apt-get install -y \
    ros-jazzy-ros2-control \
    ros-jazzy-ros2-controllers \
    ros-jazzy-gripper-controllers \
    && rm -rf /var/lib/apt/lists/*

# MoveIt 2:
RUN apt-get update && apt-get install -y \
    ros-jazzy-moveit \
    && rm -rf /var/lib/apt/lists/*

# Gazebo Simulator:
RUN apt-get update && apt-get install -y \
    curl \
    lsb-release \
    && curl -sSL https://packages.osrfoundation.org/gazebo.gpg \
        --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" \
        > /etc/apt/sources.list.d/gazebo-stable.list \
    && apt-get update && apt-get install -y \
    gz-harmonic \
    ros-jazzy-ros-gz \
    ros-jazzy-gz-ros2-control \
    && rm -rf /var/lib/apt/lists/*

# ============================================================== #
# Workspace:
# ============================================================== #

WORKDIR /dev_ws
RUN mkdir -p /dev_ws/src && \
    ln -s /dev_ws /root/dev_ws

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
        --rosdistro jazzy \
        -y && \
    rm -rf /var/lib/apt/lists/*

# UNIVERSAL ROBOTS:
RUN apt-get update && apt-get install -y \
    ros-jazzy-ur \
    && rm -rf /var/lib/apt/lists/*

# ============================================================== #
# ROSCon UK 2026 workspace sources and ros2srrc dependencies:
# ============================================================== #

WORKDIR /dev_ws/src

RUN git clone -b jazzy https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl.git

RUN git clone -b jazzy https://github.com/IFRA-Cranfield/IFRA_ObjectPose.git
RUN git clone -b jazzy https://github.com/IFRA-Cranfield/ros2_RobotiqGripper.git

RUN git clone -b jazzy https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics.git
RUN git clone -b jazzy https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics.git

# Include the local workshop checkout from the Docker build context.
COPY . /dev_ws/src/ROSCon_UK_2026/

# ============================================================== #
# Build dependencies and workspace:
# ============================================================== #

# Small step required -> Add the move_group_interface_improved.h file:
RUN cp \
    /dev_ws/src/ros2_SimRealRobotControl/include/move_group_interface_improved.h \
    /opt/ros/jazzy/include/moveit_ros_planning_interface/moveit/move_group_interface/move_group_interface_improved.hpp

# ============================================================== #
# BUILD WORKSPACE:
# ============================================================== #

WORKDIR /dev_ws
RUN /bin/bash -c \
    "source /opt/ros/jazzy/setup.bash && \
     colcon build"

# ============================================================== #
# Workshop perception: OpenCV, ROS image conversion and YOLO:
# ============================================================== #

RUN apt-get update && apt-get install -y \
    python3-venv \
    python3-pip \
    ros-jazzy-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /root/venvs/ifra_ope && \
    /root/venvs/ifra_ope/bin/python -m pip install --no-cache-dir --upgrade pip && \
    /root/venvs/ifra_ope/bin/python -m pip install --no-cache-dir \
        "numpy<2" \
        "opencv-contrib-python==4.10.0.84" \
        "ultralytics==8.4.137"

# ============================================================== #
# Runtime shell:
# ============================================================== #

RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc && \
    echo "[ -f /dev_ws/install/local_setup.bash ] && source /dev_ws/install/local_setup.bash" >> /root/.bashrc && \
    echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> /root/.bashrc

# ============================================================== #
# ROS_DOMAIN_ID -> This is the ROS 2 domain ID for your ROS 2 system. It allows you to run multiple ROS 2 systems on the same network without them interfering with each other. The default value is 0, but you can change it to any integer between 0 and 232.
# ROS_LOCALHOST_ONLY -> This means your ROS 2 system, and its topics, services, and actions will not be visible to other computers on the local network.
# ============================================================== #   

RUN echo "export ROS_DOMAIN_ID=0" >> /root/.bashrc && \ 
    echo "export ROS_LOCALHOST_ONLY=1" >> /root/.bashrc 

CMD ["bash"]
