# PART C: Integration of External Tools within the ROS 2-based Robotic System

__REFERENCES__

- https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/tree/humble-gzfortress/ros2srrc_execution/python: Location of the Python primitives (including client Robot and End-effector classes) at ros2srrc_execution.
- https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble-gzfortress/instructions/RobotOperation.md for more detail on Robot Operation and Monitoring commands and instructions.
- https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics/blob/humble-gzfortress/instructions/Examples.md for more detail about how Cranfield University's ABB IRB-120 Robot Cell is operated (irb120_CranfieldRobotics package).

## C3: Create a Pick&Place Robot Program using a .py file

In this task, you will learn how to create and execute a static sequence of Robot Movements using the ros2srrc_execution/python primitives.

__ros2srrc -> Python classes__

The `ros2srrc_execution` package provides a collection of Python primitives for operating the robot and its end-effector. These primitives are available in the [`ros2srrc_execution/python`](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/tree/humble-gzfortress/ros2srrc_execution/python) folder. Internally, the ROS 2 interfaces used to control the robot are based on the `/Move` and `/Robmove` action clients, together with ROS 2 service clients for controlling the end-effector(s). Instead of requiring the user to create and manage these action and service clients directly, the functionality is encapsulated in two Python classes: `ROBOT()` and `ENDEFFECTOR()`.

The `ROBOT()` class provides Python functions for sending robot movement commands, such as joint-space or Cartesian movements, and for monitoring their execution. The `ENDEFFECTOR()` class provides functions for operating the connected tool, such as opening and closing a gripper. These classes hide much of the underlying ROS 2 communication, allowing a Python program to control the robot using simple function calls. This is particularly useful when integrating external software or hardware written in Python, such as vision systems, sensors, object-detection algorithms, or task-planning applications. The external application can create instances of the `ROBOT()` and `ENDEFFECTOR()` classes and use their functions to communicate with and operate the ROS 2 robot system. This exercise demonstrates this approach by implementing a complete pick-and-place operation in Python.


__TASK__

In this exercise, you will:

- **Understand the Python primitives**
  - Explore how the `ROBOT()` and `ENDEFFECTOR()` classes are defined and used.
  - Learn how these classes provide a Python interface to the robot's `/Move` and `/Robmove` action servers and the end-effector's ROS 2 services.
  - Understand how robot waypoints, movement commands, and gripper operations are combined to create a complete robot program.

- **Fill in the `cubePP.py` program**
  - Complete the unfinished `cubePP.py` Python script by adding the required robot waypoints and end-effector commands.
  - The program should reproduce the same pick-and-place sequence implemented previously in `cubePP.yaml`, but using the Python primitives instead of a YAML program.
  - The sequence should move the robot to the required approach and pick positions, operate the gripper to grasp the cube, transport the cube to the placement position, release it, and return the robot to a safe position.
  - After modifying the program, rebuild the workspace so that the updated executable is installed:
  
    ```sh
    cd ~/dev_ws
    colcon build
    ```

- **Execute the Python program**
  - Launch the ROS 2 robot-cell environment and spawn the cube in Gazebo.
  - Run the completed program using `ros2 run rosconuk26 cubePP.py`.
  - Observe how the Python script communicates with the robot and end-effector through the `ROBOT()` and `ENDEFFECTOR()` classes.
  - Confirm that the robot successfully picks up the cube, places it at the target location, and completes the programmed sequence.

</br>

_Execution Steps (cubePP.py program)_

1. Fill in the .py files with the specified robot waypoints. After doing the changes in the Robot Program file, the ROS 2 Workspace must be compiled in order to save the changes --> In a new terminal shell, COLCON BUILD:
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
    ros2 run rosconuk26 cubePP.py
    ```

5. You can now close the ROS 2 Environment.

</br>
</br>

---

</br>
</br>

### SOLUTION

The solution of cubePP.py is located in the /solutions folder. Remember to build the ROS 2 workspace after making any changes to the robot programs!
