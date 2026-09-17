# Installation - Ubuntu 22.04 PC

This workshop is based on [ros2_SimRealRobotControl (ros2srrc)](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl), an open-source framework developed by the IFRA-Cranfield Research Group at Cranfield University. It brings together ROS 2, Gazebo and MoveIt 2 to support robot simulation, motion planning and real robot control through a modular structure of robot models, controllers and end-effector configurations.

The repository is available in three versions:

- **ROS 2 Humble with Gazebo Classic** — the [`humble` branch](https://github.com/IFRA-Cranfield/ROSCon_UK_2026).
- **ROS 2 Humble with Gazebo Fortress** — the [`humble-gzfortress` branch](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/humble-gzfortress).
- **ROS 2 Jazzy with Gazebo Harmonic** — the [`jazzy` branch](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/jazzy).

This installation guide targets **Ubuntu 22.04, ROS 2 Humble and Gazebo Classic**. The procedure is divided into five parts, which should be completed in order:

- **Part A:** Set up the standard ROS 2 environment for robot simulation, motion planning and control.
- **Part B:** Install the ROS 2 drivers required to interface with ABB and Universal Robots hardware.
- **Part C:** Install the ros2srrc framework, its supporting packages and the robot configurations used in the workshop.
- **Part D:** Install the computer vision libraries required for object detection and position estimation.
- **Part E:** Download and build the workshop repository.

## PART A: Install ROS 2 Humble for Robot Arm Simulation and Control

This section establishes the standard software environment for robot arm simulation and control using ROS 2. It covers the installation of ROS 2 Humble, Gazebo Classic, `ros2_control`, ROS 2 controllers and MoveIt 2, together with the development tools and workspace configuration required to build and run ROS 2 packages.

These components provide the foundation for the workshop: ROS 2 enables communication between software components, Gazebo simulates the robot and its environment, `ros2_control` provides the controller infrastructure, and MoveIt 2 supports motion planning and trajectory execution.

1. Install Ubuntu 22.04: https://ubuntu.com/desktop

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

3. Install ROS 2 Humble:
    - Follow instructions in: [ROS 2 Humble Tutorials - Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).
    - Source the ROS 2 Humble installation in the .bashrc file (hidden file in /home):
        ```sh
        source /opt/ros/humble/setup.bash
        ```

4. Install MoveIt 2 for ROS 2 Humble ([REF: MoveIt 2 Website](https://moveit.picknik.ai/humble/index.html)):

    ```sh
    # Command for BINARY INSTALL (recommended):
    sudo apt install ros-humble-moveit
    ```

5. Create and configure the ROS 2 Humble ~/dev_ws environment/workspace:
    - Follow instructions in: [ROS 2 Humble Tutorials - Create a ROS 2 Workspace](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).
    - Source the ~/dev_ws workspace in .bashrc file:
        ```sh
        source ~/dev_ws/install/local_setup.bash
        ```

6. Install ROS 2 packages, which are required for ROS 2-based Robot Simulation and Control:

    ```sh
    # Install ROS 2 Development Tools:
    sudo apt install ros-dev-tools
    sudo apt install ros-humble-xacro

    # ROS 2 Control + ROS 2 Controllers:
    sudo apt install ros-humble-ros2-control
    sudo apt install ros-humble-ros2-controllers
    sudo apt install ros-humble-gripper-controllers

    # Gazebo for ROS 2 Humble:
    sudo apt install gazebo
    sudo apt install ros-humble-gazebo-ros2-control
    sudo apt install ros-humble-gazebo-ros-pkgs

    # xacro:
    sudo apt install ros-humble-xacro

    # Install CycloneDDS RMW for ROS 2 Humble to fix cycle time issues in humble-moveit (temporary fix):
    sudo apt install ros-humble-rmw-cyclonedds-cpp
    # Add the following statement into .bashrc file:
    export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
    ```

    (EXTRA STEP) -> Due to problems with URDF file processing in the newest version of the Gazebo ROS 2 Control plugin, `gazebo_ros2_control` must be downgraded to version 0.4.6:

    ```sh
    # Uninstall Gazebo ROS 2 Control:
    sudo apt remove ros-humble-gazebo-ros2-control

    # Download and install the 0.4.6 version:
    cd ~/dev_ws/src
    git clone https://github.com/ros-controls/gazebo_ros2_control.git
    cd gazebo_ros2_control
    git reset --hard 9a3736c # Commit for the 0.4.6 version!
    cd ~/dev_ws
    colcon build
    ```

## PART B: Download and install proprietary ROS 2 Drivers for ABB and UR robots

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

8. __Universal Robots ROS 2 Driver__: The installation of the [ur-robot-driver](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver) is required for the control of any real UR robot using ROS 2. Binary install, for ROS 2 Humble:

    ```sh
    sudo apt-get install ros-humble-ur
    ```

## PART C: Install IFRA-Cranfield's ros2_SimRealRobotControl ROS 2 Framework

This section installs the ros2srrc framework and the additional IFRA-Cranfield packages required for its operation. These supporting packages provide functionality for interacting with objects in simulation, obtaining object and link poses, and controlling supported grippers.

The installation also includes the modified MoveIt 2 interface required by ros2srrc’s robot movement functions, followed by the framework build and the installation of dedicated packages for the ABB IRB-120 and UR3 Cranfield robotic cells.

9. Import and install the following ROS 2 Packages developed by IFRA-Cranfield:

    ```sh
    # IFRA-Cranfield/IFRA_LinkAttacher:
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/IFRA_LinkAttacher.git

    # IFRA-Cranfield/IFRA_ObjectPose:
    git clone https://github.com/IFRA-Cranfield/IFRA_ObjectPose.git

    # IFRA-Cranfield/IFRA_LinkPose:
    git clone https://github.com/IFRA-Cranfield/IFRA_LinkPose.git

    # IFRA-Cranfield/ros2_RobotiqGripper:
    git clone https://github.com/IFRA-Cranfield/ros2_RobotiqGripper.git

    # Build:
    cd ~/dev_ws
    colcon build
    ```

10. Download the ros2_SimRealRobotControl repository:

    ```sh
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl
    ```

11. Modify the move_group_interface.h script: A modified version of the move_group_interface.h file is required in order to execute the MoveIt 2-based Robot Movements in ros2_SimRealRobotControl. Both the upgraded file and the instructions of how to implement it can be found here: [move_group_interface_improved.h](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/tree/humble/include), but you can as well directly execute this step by running the following command:

    ```sh
    sudo cp ~/dev_ws/src/ros2_SimRealRobotControl/include/move_group_interface_improved.h /opt/ros/humble/include/moveit/move_group_interface/move_group_interface_improved.h
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
    git clone https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics.git

    # IFRA-Cranfield/ur3_CranfieldRobotics:
    cd ~/dev_ws/src
    git clone https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics.git

    # Build:
    cd ~/dev_ws
    colcon build
    ```

## PART D: Install OpenCV and YOLO for Object Detection and Pose Estimation Tasks

Some workshop exercises use camera images to detect objects and estimate their positions before executing robot movements. These tasks require **YOLO**, installed through the Ultralytics package, for object detection, and **OpenCV** for image processing and ArUco marker detection.

Installing these libraries enables the perception components used in the workshop’s vision-guided pick-and-place exercise.

```sh
# Install pip:
sudo apt-get install python3-pip

# Install OpenCV and YOLO:
python3 -m pip install "numpy<2" opencv-contrib-python ultralytics

# Install ROS 2 <-> OpenCV bridge:
sudo apt-get install ros-humble-cv-bridge
```

## PART E: Install the IFRA-Cranfield/ROSCon_UK_2026 repository

The final section downloads the **ROSCon_UK_2026** workshop repository into the ROS 2 workspace and builds its package using `colcon`. The repository contains the robot cell configurations, simulation resources, example programs and perception scripts used throughout the practical exercises.

Completing this step makes the workshop resources available within the configured ROS 2 environment.

```sh
# IFRA-Cranfield/ROSCon_UK_2026:
cd ~/dev_ws/src
git clone https://github.com/IFRA-Cranfield/ROSCon_UK_2026.git

# Build:
cd ~/dev_ws
colcon build
```