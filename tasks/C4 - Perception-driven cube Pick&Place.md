# PART C: Integration of External Tools within the ROS 2-based Robotic System

__REFERENCES__

- https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics/tree/jazzy/irb120cranfield_ope -> Location of the object pose estimation package for the ABB IRB-120 Cranfield University Cell.
- https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics/blob/jazzy/instructions/Examples.md for more detail about how the irb120cranfield_ope is executed. 
- https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics/tree/jazzy/ur3cranfield_ope -> Location of the object pose estimation package for the UR3 Cranfield University Cell.
- https://github.com/IFRA-Cranfield/ur3_CranfieldRobotics/blob/jazzy/instructions/Examples.md for more detail about how the ur3cranfield_ope is executed. 

## C4: Object detection, pose estimation, and pick-and-place using YOLO and OpenCV in ROS 2

In this task, you will learn how to combine OpenCV, YOLO and the Python primitives learnt in C3 to obtain an object detection, pose estimation and pick-and-place task using ROS 2 and Python.

__ros2srrc -> Integration of YOLO and OpenCV__

In this exercise, OpenCV, YOLO, and the Python primitives provided by `ros2srrc_execution` are combined to demonstrate a complete perception-driven cube pick-and-place application. 

YOLO is used to detect the cubes in the camera image and identify their colours. 

OpenCV is then used for cube pose estimation in two stages. First, an ArUco-grid calibration is performed to establish the relationship between image pixels and real-world distances within the ABB IRB-120 robot cell. Secondly, image processing and filtering techniques are applied to determine the centre of each detected cube in the image. The pixel-to-millimetre conversion obtained during calibration is then used to estimate the position of each cube within the robot cell. 

Once a cube's position has been estimated, its coordinates are provided as input to the `ROBOT()` class from `ros2srrc_execution`. The robot can then use these coordinates to execute the required pick-and-place operation.

The perception and robot-operation functionality are distributed across three Python scripts located in the package's `ope` folder:

- **`arucoGRID.py`**
  - Contains the functions required to detect the ArUco markers.
  - Uses the known geometry of the ArUco grid to calibrate the camera view.
  - Calculates the pixel-to-distance conversion required to convert image coordinates into real-world coordinates for the robot cell.

- **`PositionEstimation.py`**
  - Performs cube detection using the YOLO model.
  - Identifies the colour and image location of each detected cube.
  - Uses the ArUco calibration data together with OpenCV image processing and filtering to estimate the position of each cube within the robot cell.
  - Publishes the execution-time state and estimated position of all detected cubes to ROS 2 topics.
  - This node must be running before the pick-and-place program so that cube detection and position information are available.

- **`cubePP_detection.py`**
  - Subscribes to the ROS 2 topics published by `PositionEstimation.py`.
  - Receives the current state and estimated position of the selected cube.
  - Checks whether the requested cube has been detected.
  - Uses the `ROBOT()` and `ENDEFFECTOR()` Python classes to perform the pick-and-place operation when valid position data is available.
  - Receives the selected cube through the `cube` command-line argument, allowing different detected cubes to be chosen by colour or name.

The YOLO model (trained using images labelled using RoboFlow) used for cube detection is stored in the `ope/yolo` folder. It is loaded by the perception node and is responsible for detecting the cubes and distinguishing their colours.


__TASK__

In this exercise, you will:

- **Understand the integration of external software and hardware**
  - Understand how external perception software, such as YOLO and OpenCV, can be integrated into a ROS 2-based robotic system using Python.
  - Learn how camera images are processed to detect cubes, identify their colours, and estimate their positions.
  - Understand how ArUco markers are used to calibrate the camera and convert image coordinates into coordinates related to the robot cell.
  - Observe how perception data is published through ROS 2 topics and consumed by another Python node.
  - Understand how the estimated cube coordinates are passed to the `ROBOT()` class to coordinate perception with robot motion and execute a specific pick-and-place application.

- **Execute the perception-driven pick-and-place task**
  - Launch the ROS 2 simulation environment and spawn one or more cubes in the robot cell.
  - Move the robot to a suitable pose where the complete ArUco grid is visible to the camera.
  - Execute `PositionEstimation.py` to start YOLO-based cube detection, ArUco calibration, pose estimation, and publication of the detected-cube states.
  - Execute `cubePP_detection.py` with the required cube name, such as `BlueCube`, `GreenCube`, `RedCube`, or `WhiteCube`.
  - The pick-and-place node obtains the selected cube's estimated position from its ROS 2 topics and uses the robot and end-effector Python primitives to pick and place it.
  - Repeat the process for different cube colours and observe how the same program can select different detected cubes at run time.

</br>

_Execution Steps (PositionEstimation.py first, cubePP_detection.py second)_

```sh
# 1. Launch the simulation environment:
ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_3

# 2. Spawn cubes within the environment (feel free to modify the x,y values):
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "RedCube.sdf" --name "RedCube" --x 0.60 --y 0.70 --z 0.95
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "BlueCube.sdf" --name "BlueCube" --x 0.70 --y 0.70 --z 0.95
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "WhiteCube.sdf" --name "WhiteCube" --x 0.60 --y 0.60 --z 0.95
ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "GreenCube.sdf" --name "GreenCube" --x 0.70 --y 0.60 --z 0.95

# 3. Please note that, for the PositionEstimation node to work properly, the ArUco grid must be completely visible! A safe pose would be:
ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveJ', movej: {joint1: 0.00, joint2: -30.00, joint3: 30.00, joint4: 0.00, joint5: 90.00, joint6: 0.00}, speed: 1.0}"

# 4. Execute the Cube Detection and Pose Estimation script:
source ~/venvs/ifra_ope/bin/activate
python3 "$HOME/dev_ws/src/ROSCon_UK_2026/rosconuk26/ope/PositionEstimation.py" model:=cubedetection_irb120 visualize:=true

# 5. Execute the program:
ros2 run rosconuk26 cubePP_detection.py cube:=BlueCube
ros2 run rosconuk26 cubePP_detection.py cube:=GreenCube
ros2 run rosconuk26 cubePP_detection.py cube:=RedCube
ros2 run rosconuk26 cubePP_detection.py cube:=WhiteCube

# EXTRA: Once the cubes have been placed, you should be able to monitor their estimated position using:
ros2 topic list
# From the (absolute truth) GzSim plugin:
ros2 topic echo /BlueCube/ObjectPose
ros2 topic echo /GreenCube/ObjectPose
ros2 topic echo /RedCube/ObjectPose
ros2 topic echo /WhiteCube/ObjectPose
# From the object pose estimation ROS 2 node:
ros2 topic echo /BlueCube/ObjectPoseEstimation
ros2 topic echo /GreenCube/ObjectPoseEstimation
ros2 topic echo /RedCube/ObjectPoseEstimation
ros2 topic echo /WhiteCube/ObjectPoseEstimation
```
