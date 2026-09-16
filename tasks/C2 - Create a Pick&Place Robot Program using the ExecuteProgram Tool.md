# PART C: Integration of External Tools within the ROS 2-based Robotic System

__REFERENCES__

- https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/jazzy/instructions/ProgramExecution.md for more detailed instructions on how Robot Programs are executed using the __ExecuteProgram__ tool.
- https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/jazzy/instructions/RobotOperation.md for more detail on Robot Operation and Monitoring commands and instructions.
- https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics/blob/jazzy/instructions/Examples.md for more detail about how Cranfield University's ABB IRB-120 Robot Cell is operated (irb120_CranfieldRobotics package).

## C2: Create a Pick&Place Robot Program using the ExecuteProgram Tool

In this task, you will learn how to create and execute a static sequence of Robot Movements using the ros2srrc_execution/ExecuteProgram tool.

__ExecuteProgram Tool__

ExecuteProgram.py is a Python script designed to automate the execution of static robotic programs within our ROS 2 environment. It is responsible for interpreting and executing predefined sequences of robot movements or actions stored in a .yaml file located within a specific ROS 2 package. These programs, written in YAML format, define a series of sequential steps to control robotic joints, grippers, or any other components involved in a given task.

Upon invocation, the script reads the specified program file (e.g., PROGRAM_NAME.yaml), which must be located in the /programs folder of any ROS 2 package. The following command must be used to execute a Robot Program:

```sh
ros2 run ros2srrc_execution ExecuteProgram.py package:="PACKAGE-NAME" program:="PROGRAM-NAME"
```

- _PACKAGE-NAME_: The name of the ROS 2 Package where your program is located (inside the /programs folder).
- _PROGRAM-NAME_: The name of the program you want to execute (without the .yaml extension).

__TASK__

In this exercise, you will:

- Execute the demo program, to understand how Robot Programs are executed with the ExecuteProgram.py tool.
- Fill in the Robot Movement waypoints in the cubePP.yaml file, and execute the programs to perform the Cube Pick&Place task. The exact waypoint values (required robot poses) are included below.

</br>

_Execution Steps (demo Program)_

1. Launch the ROSConUK26 ABB IRB-120 Gazebo + MoveIt 2 Environment:
    ```sh
    ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_1
    ```

2. Execute the demo Program:
    ```sh
    ros2 run ros2srrc_execution ExecuteProgram.py package:=rosconuk26 program:=demo
    ```

3. You can now close the ROS 2 Environment.

</br>

_Execution Steps (cubePP Program)_

1. Fill in the cubePP.yaml file with the specified values. After doing the changes in the Robot Program files, the ROS 2 Workspace must be compiled in order to save the changes --> In a new terminal shell, COLCON BUILD:
    ```sh
    cd ~/dev_ws
    colcon build
    ```

2. Launch the ROSConUK26 ABB IRB-120 Gazebo + MoveIt 2 Environment:
    ```sh
    ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_2  # Robot w/ gripper.
    ```

3. Spawn the BlackCube to the Simulation Environment, to the following location:
    ```sh
    ros2 run ros2srrc_execution SpawnObject.py --package "rosconuk26" --sdf "BlackCube.sdf" --name "BlackCube" --x 0.60 --y 0.70 --z 0.95
    ```

4. Execute the CubePP Robot Program:
    ```sh
    ros2 run ros2srrc_execution ExecuteProgram.py package:=rosconuk26 program:=cubePP
    ```

5. You can now close the ROS 2 Environment.

</br>
</br>

---

</br>
</br>

### SOLUTION

The solution of cubePP.yaml is located in the /solutions folder. Remember to build the ROS 2 workspace after making any changes to the robot programs!