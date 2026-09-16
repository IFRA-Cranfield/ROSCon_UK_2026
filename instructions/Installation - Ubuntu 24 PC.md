# Installation - Ubuntu 24.04 PC

This workshop is based on [ros2_SimRealRobotControl (ros2srrc)](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/tree/jazzy), an open-source framework developed by the IFRA-Cranfield Research Group at Cranfield University. It brings together ROS 2, Gazebo and MoveIt 2 to support robot simulation, motion planning and real robot control through a modular structure of robot models, controllers and end-effector configurations.

The repository is available in three versions:

- **ROS 2 Humble with Gazebo Classic** — the [`humble` branch](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/humble).
- **ROS 2 Humble with Gazebo Fortress** — the [`humble-gzfortress` branch](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/humble-gzfortress).
- **ROS 2 Jazzy with Gazebo Harmonic** — the [`jazzy` branch](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/jazzy).

This installation guide targets **Ubuntu 24.04, ROS 2 Jazzy and Gazebo Harmonic**. The procedure is divided into five parts, which should be completed in order:

- **Part A:** Set up the standard ROS 2 environment for robot simulation, motion planning and control.
- **Part B:** Install the ROS 2 drivers required to interface with ABB and Universal Robots hardware.
- **Part C:** Install the ros2srrc framework, its supporting packages and the robot configurations used in the workshop.
- **Part D:** Install the computer vision libraries required for object detection and position estimation.
- **Part E:** Download and build the workshop repository.

## PART A: Install ROS 2 Jazzy for Robot Arm Simulation and Control

This section establishes the standard software environment for robot arm simulation and control using ROS 2. It covers the installation of ROS 2 Jazzy, Gazebo Harmonic, `ros2_control`, ROS 2 controllers and MoveIt 2, together with the development tools and workspace configuration required to build and run ROS 2 packages.

These components provide the foundation for the workshop: ROS 2 enables communication between software components, Gazebo simulates the robot and its environment, `ros2_control` provides the controller infrastructure, and MoveIt 2 supports motion planning and trajectory execution.

1. Install Ubuntu 24.04: https://ubuntu.com/desktop

2. Install Git:

    ```sh
    # In the terminal shell:
    sudo apt install git

    # Git account configuration:
    git config --global user.name YourUsername
    git config --global user.email YourEmail
    git config --global color.ui true
    git config --global core.editor code --wait # Visual Studio Code is recommended.
    git config --global credential.helper store
    ```

3. Install ROS 2 Jazzy:
    - Follow instructions in: [ROS 2 Jazzy Tutorials - Installation](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html).
    - Source the ROS 2 Jazzy installation in the .bashrc file (hidden file in /home):
        ```sh
        source /opt/ros/jazzy/setup.bash
        ```

4. Install MoveIt 2 for ROS 2 Jazzy ([REF: MoveIt 2 Website](https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html)):

    ```sh
    # Command for BINARY INSTALL (recommended):
    sudo apt install ros-jazzy-moveit
    ```

5. Create and configure the ROS 2 Jazzy ~/dev_ws environment/workspace:
    - Follow instructions in: [ROS 2 Jazzy Tutorials - Create a ROS 2 Workspace](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).
    - Source the ~/dev_ws workspace in .bashrc file:
        ```sh
        source ~/dev_ws/install/local_setup.bash
        ```

6. Install ROS 2 packages, which are required for ROS 2-based Robot Simulation and Control:

    ```sh
    # Install ROS 2 Development Tools:
    sudo apt install ros-dev-tools
    sudo apt install ros-jazzy-xacro

    # ROS 2 Control + ROS 2 Controllers:
    sudo apt install ros-jazzy-ros2-control
    sudo apt install ros-jazzy-ros2-controllers
    sudo apt install ros-jazzy-gripper-controllers

    # Gazebo Harmonic for ROS 2 Jazzy:
    sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
    sudo apt-get update
    sudo apt-get install gz-harmonic
    
    # Gazebo Harmonic <-> ROS 2 Pairings:
    sudo apt install ros-jazzy-ros-gz
    sudo apt install ros-jazzy-gz-ros2-control

    # Install CycloneDDS RMW for ROS 2 Jazzy to fix cycle time issues in jazzy-moveit:
    sudo apt install ros-jazzy-rmw-cyclonedds-cpp 
    # Add the following statement into .bashrc file: 
    export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
    ```

## PART B: Download and install ROS 2 Drivers for ABB and UR robots

Although ros2srrc supports a range of robot models in simulation, real robot control through the framework has so far been tested only with ABB and Universal Robots (UR) hardware. This section therefore installs the corresponding ROS 2 drivers, which provide the communication interfaces needed to send commands to physical robots and receive feedback from their controllers.

Future development aims to extend and validate real robot control across additional models and manufacturers, including FANUC, KUKA, Comau, Dobot...

7. __ABB driver for ROS 2__: The installation of the [abb_ros2](https://github.com/PickNikRobotics/abb_ros2) driver is required for the control of any real ABB robot using ROS 2.

    ```sh
    mkdir -p ~/dev_ws/src/ABBDriver
    cd ~/dev_ws/src/ABBDriver
    git clone https://github.com/PickNikRobotics/abb_ros2.git -b rolling
    sudo rosdep init
    rosdep update
    vcs import < abb_ros2/abb.repos
    rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
    cd ~/dev_ws
    colcon build
    ```

8. __Universal Robots ROS 2 Driver__: The installation of the [ur-robot-driver](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver) is required for the control of any real UR robot using ROS 2. Binary install, for ROS 2 Jazzy:

    ```sh
    sudo apt-get install ros-jazzy-ur
    ```

## PART C: Install IFRA-Cranfield's ros2_SimRealRobotControl ROS 2 Framework

This section installs the ros2srrc framework and the additional IFRA-Cranfield packages required for its operation. These supporting packages provide functionality for interacting with objects in simulation, obtaining object and link poses, and controlling supported grippers.

The installation also includes the modified MoveIt 2 interface required by ros2srrc’s robot movement functions, followed by the framework build and the installation of dedicated packages for the ABB IRB-120 and UR3 Cranfield robotic cells.

9. Import and install the following ROS 2 Packages developed by IFRA-Cranfield:

    ```sh
    # IFRA-Cranfield/IFRA_ObjectPose:
    cd ~/dev_ws/src
    git clone -b jazzy https://github.com/IFRA-Cranfield/IFRA_ObjectPose.git

    # IFRA-Cranfield/ros2_RobotiqGripper:
    git clone -b jazzy https://github.com/IFRA-Cranfield/ros2_RobotiqGripper.git
    
    # Build the workspace:
    cd ~/dev_ws
    colcon build
    ```

10. Download the ros2_SimRealRobotControl repository:

    ```sh
    cd ~/dev_ws/src
    git clone -b jazzy https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl
    ```

11. Modify the move_group_interface.h script: A modified version of the move_group_interface.h file is required in order to execute the MoveIt 2-based Robot Movements in ros2_SimRealRobotControl. Both the upgraded file and the instructions of how to implement it can be found here: [move_group_interface_improved.h](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/tree/jazzy/include), but you can as well directly execute this step by running the following command:

    ```sh
    sudo cp ~/dev_ws/src/ros2_SimRealRobotControl/include/move_group_interface_improved.h /opt/ros/jazzy/include/moveit_ros_planning_interface/moveit/move_group_interface/move_group_interface_improved.hpp
    ```

12. Build the workspace:

    ```sh
    cd ~/dev_ws
    colcon build
    ```

13. Download and install IFRA-Cranfield's dedicated ROS 2 Packages for the ABB IRB-120 and UR3 robots:

    ```sh
    # IFRA-Cranfield/irb120_CranfieldRobotics:
    cd ~/dev_ws/src
    git clone -b jazzy https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics.git

    # IFRA-Cranfield/ur3_CranfieldRobotics:
    cd ~/dev_ws/src
    git clone -b jazzy https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics.git

    # Build:
    cd ~/dev_ws
    colcon build
    ```

## PART D: Install OpenCV and YOLO for Object Detection and Pose Estimation Tasks

Some workshop exercises use camera images to detect objects and estimate their positions before executing robot movements. These tasks require **YOLO**, installed through the Ultralytics package, for object detection, and **OpenCV** for image processing and ArUco marker detection.

Installing these libraries enables the perception components used in the workshop’s vision-guided pick-and-place exercise.

```sh
# Install Python3 venv, pip and cv_bridge for ROS 2:
sudo apt-get install python3-venv 
sudo apt-get install python3-pip 
sudo apt-get install ros-jazzy-cv-bridge 

# Create a Python3 virtual environment and install the required packages:
python3 -m venv ~/venvs/ifra_ope
source ~/venvs/ifra_ope/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install "numpy<2" "opencv-contrib-python==4.10.0.84" "ultralytics==8.4.137"
```

## PART E: Install the IFRA-Cranfield/ROSCon_UK_2026 repository

The final section downloads the **ROSCon_UK_2026** workshop repository into the ROS 2 workspace and builds its package using `colcon`. The repository contains the robot cell configurations, simulation resources, example programs and perception scripts used throughout the practical exercises.

Completing this step makes the workshop resources available within the configured ROS 2 environment.

```sh
# IFRA-Cranfield/ROSCon_UK_2026:
cd ~/dev_ws/src
git clone https://github.com/IFRA-Cranfield/ROSCon_UK_2026.git -b jazzy

# Build:
cd ~/dev_ws
colcon build
```
