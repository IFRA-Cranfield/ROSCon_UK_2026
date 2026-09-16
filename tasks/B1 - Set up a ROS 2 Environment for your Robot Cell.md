# PART B: Setting up your own Robot Cell using IFRA's ROS 2 Packages

__REFERENCES__

- https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble-gzfortress/instructions/ROS2EnvironmentLaunch.md for better detail about the ROS 2 Environment Launch process.
- https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics/tree/humble-gzfortress for more detail about how the ROS 2 Gazebo + MoveIt 2 Packages were built for Cranfield University's ABB IRB-120 Robot Cell.
- https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics/tree/humble-gzfortress for more detail about how the ROS 2 Gazebo + MoveIt 2 Packages were built for Cranfield University's UR3 Robot Cell.

</br>

## B1: Set up a ROS 2 Environment for your Robot Cell

Every time a new ROS 2 environment is created for a custom robot cell based on the `ros2srrc` packages, a single ROS 2 package must be created for that robot cell. This package acts as the central container for the cell's configurations, robot descriptions, CAD models, static programs, and any additional custom functionality.

The package should follow the standard ROS 2 package structure and contain the following elements:

- **`package.xml` and `CMakeLists.txt`**
  - These are required by the standard ROS 2 package conventions.
  - `package.xml` describes the package metadata and its dependencies.
  - `CMakeLists.txt` defines how the package is built and which files, folders, launch files, or resources are installed.

- **`config` folder**
  - This folder contains the `configurations.yaml` file.
  - The YAML file defines the different robot-cell layouts or configurations available in the package.
  - Each configuration specifies the relevant id, robot, end-effector, and URDF file required to launch that particular cell variation.

- **`meshes` folder**
  - This folder contains the custom CAD files used to represent the robot cell and its components.
  - These files may include `.dae`, `.stl`, or other mesh formats.
  - The meshes are referenced by the URDF files to provide visual and collision models for objects such as tables, stands, fixtures, tools, and other equipment.

- **`urdf` folder**
  - This folder contains the URDF or Xacro descriptions of the robot-cell configurations.
  - These files also define how standard robot and end-effector descriptions from the `ros2srrc_robots` and `ros2srrc_endeffectors` packages are imported, positioned, and connected to the rest of the environment.

- **`sdf` folder**
  - This folder contains the SDF model descriptions used to spawn objects in Gazebo Sim.
  - These files define each object's physical properties, visual and collision meshes, and any Gazebo Sim plugins associated with it.
  - In this repository, the colour-specific cube files (`BlueCube.sdf`, `GreenCube.sdf`, `RedCube.sdf`, `WhiteCube.sdf`, and `BlackCube.sdf`) define the cube models used in the pick-and-place and object-pose estimation use cases.

- **`programs` folder (optional)**
  - This folder can be used to store static robot programs.
  - The programs can be executed using the `ExecuteProgram` node provided by the `ros2srrc_execution` package.
  - This is useful for storing predefined robot behaviours, demonstrations, or task sequences associated with a particular robot-cell configuration.

- **Additional custom functionality**
  - Any custom ROS 2 node required for application-specific functionality should be stored in a separate, dedicated folder within the package.
  - The exact folder name and internal structure can be chosen according to the needs of the application.
  - In this repository, the object-detection ROS 2 node is stored in the `ope` folder, which contains the corresponding Python scripts and supporting files.

</br>

This exercise consists of 4 different tasks:

### 1. Understanding the configurations.yaml file

Spend some time understanding the rosconuk26/config/configurations.yaml file. This file contains the description of all different Robot Cell layout variations, and its links to the Robot Cell's URDF files.

### 2. Understanding the structure of the URDF files

Have a look into the Robot Cell's URDF files. Pay special attention to:

- How the ROBOT's and END-EFFECTOR's standard URDF's are imported from ros2srrc_robots and ros2srrc_endeffectors repositories.
- How the world/irb120enclosure components are imported to the URDF, and how the robot is linked and positioned on top of the Robot Stand.
- How the CAD files are imported to the URDF.

### 3. Launch the ROSConUK26 ABB IRB-120 Cell's ROS 2 Environment!

From PART A, we know that a Gazebo + MoveIt 2 ROS 2 Environment can be launched using the following command:

```sh
ros2 launch ros2srrc_launch moveit2.launch.py package:=PACKAGE_NAME config:=CONFIG_NAME
```

- For our IRB-120 Robot Cell in this repository, which parameter values correspond to PACKAGE_NAME and CONFIG_NAME?
- How many Robot Cell layouts/variants do we have?

</br>
</br>

---

</br>
</br>

### SOLUTION

```sh
# Gazebo Simulation:
ros2 launch ros2srrc_launch simulation.launch.py package:=rosconuk26 config:=rosconuk26_1
ros2 launch ros2srrc_launch simulation.launch.py package:=rosconuk26 config:=rosconuk26_2
ros2 launch ros2srrc_launch simulation.launch.py package:=rosconuk26 config:=rosconuk26_3

# Gazebo Simulation + MoveIt 2 Framework:
ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_1
ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_2
ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_3
```
