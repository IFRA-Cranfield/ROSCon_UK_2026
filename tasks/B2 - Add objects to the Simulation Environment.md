# PART B: Setting up your own Robot Cell using IFRA's ROS 2 Packages

__REFERENCE__

- https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/jazzy/instructions/RobotOperation.md (bottom lines) for better detail about the ROS 2 Gazebo environment object spawn process.

</br>

## B2: Add objects to the Simulation Environment

All the FIXED components of a Robot Cell (e.g. Robot Stand, Fixed Boxes, Cameras...) can be included inside the Robot's URDF. These components are fixed during the whole simulation process, and can be imported as physical entities and linked to the environment as fixed joints in the URDF.

However, this is not the case for all the moving/manipulated objects, such as the coloured cubes (objects used in this repository). These need to be represented as individual SDF files, and spawned into the Gazebo Simulation Environment using a dedicated ROS 2 Node.

This exercise consists of 2 different tasks:

### 1. Understanding object's SDF file structure

Take some time understanding how:

- Object CAD files are included inside the /meshes folder.
- Object SDF files are included inside the /sdf folder.

Please do take a look into the object SDF files:

- How the physical parameters of the object are defined.
- How the CAD files are imported into the SDF files.
- How the cube name is used throughout each SDF file.

### 2. Spawn objects to the ROSConUK26 ABB IRB-120 Cell's Gazebo Simulation Environment

In ros2_SimRealRobotControl, we use the following command to spawn objects into the Gazebo Simulation Environment:

```bash
ros2 run ros2srrc_execution SpawnObject.py --package "{}" --sdf "{}.sdf" --name "{}" --x {} --y {} --z {}
```

For this command to work properly, the SDF files of the objects to spawn have to be located inside the /sdf folder of a ROS 2 Package. Then:

- package: The name of the ROS 2 Package -> rosconuk26
- sdf: The name of the SDF file -> `BlueCube.sdf`, `GreenCube.sdf`, `RedCube.sdf`, `WhiteCube.sdf`, or `BlackCube.sdf`.
- name: The spawned object name. Use the matching cube name, such as `BlueCube`, `GreenCube`, `RedCube`, `WhiteCube`, or `BlackCube`.
- x, y, z: 3D-coordinates where the object is spawned.

__TASK__

1. Launch the ROS 2 Gazebo Simulation Environment of the ROSConUK26 ABB IRB-120 Robot Cell (learned in B1).
2. Open a new Terminal Shell, and spawn any coloured cube on top of the IRB-120 Cell Enclosure. 

    NOTE: The units are (m) and the origin is in the centre of the robot's base link, ground level.

</br>
</br>

---

</br>
</br>

### SOLUTION

Launch the Gazebo Simulation environment (any of these 2):
```sh
ros2 launch ros2srrc_launch simulation.launch.py package:=rosconuk26 config:=rosconuk26_1
ros2 launch ros2srrc_launch simulation.launch.py package:=rosconuk26 config:=rosconuk26_2
```

After launching the simulation environment, you can spawn one or more objects within the Robot Cell:
```sh
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "RedCube.sdf" --name "RedCube" --x 0.60 --y 0.70 --z 0.95
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "BlueCube.sdf" --name "BlueCube" --x 0.70 --y 0.70 --z 0.95
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "WhiteCube.sdf" --name "WhiteCube" --x 0.60 --y 0.60 --z 0.95
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "GreenCube.sdf" --name "GreenCube" --x 0.70 --y 0.80 --z 0.95
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "BlackCube.sdf" --name "BlackCube" --x 0.70 --y 0.60 --z 0.95
```

Feel free to play and change the x, y, and z values!
