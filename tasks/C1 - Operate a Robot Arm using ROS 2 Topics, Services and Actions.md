# PART C: Integration of External Tools within the ROS 2-based Robotic System

__REFERENCES__

- https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble/instructions/RobotOperation.md for more detail on Robot Operation and Monitoring commands and instructions.
- https://github.com/IFRA-Cranfield/irb120_CranfieldRobotics/blob/humble/instructions/Examples.md for more detail about how Cranfield University's ABB IRB-120 Robot Cell is operated (irb120_CranfieldRobotics package).

## C1: Operate a Robot Manipulator using ROS 2 Topics, Services and Actions

In this exercise you will learn how any Robot Arm can be monitored and controlled in ROS 2, using ROS 2 native tools in Ubuntu's Terminal Shell.

All the information about what these tools are (and how they are executed) is described below.

You will have to follow these steps:

1. Launch the ROSConUK26 ABB IRB-120 Robot Cell's Gazebo + MoveIt 2 Simulation Environment:
    ```sh
    ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_2  # IRB-120 + Schunk EGP-64 Gripper.
    ```
2. In a new Terminal Shell, execute the Robot Monitoring ROS 2 Subscriber Nodes (/Robpose and /joint_states).
3. In another Terminal Shell, execute the Robot Movement ROS 2 Actions (/Move and /RobMove).

__NOTE: After testing some movements in the ABB IRB-120, feel free to launch the Gazebo+MoveIt 2 Environment for other Robot Manipulators (Exercise A2), and test the ROS 2 Tools in them!__

## Robot Operation: Guidance

### Robot State monitoring using ROS 2 Topics (/RobPose & /joint_states)

Monitoring the robot’s state and pose is crucial for real-time feedback and system control. There are two main tools for this:

- /Robpose ROS 2 Topic.
- /joint_states ROS 2 Topic.

The /Robpose topic publishes the execution-time pose of the robot’s end-effector in terms of position and orientation. You can monitor the current pose by subscribing to this topic:
```sh
ros2 topic echo /Robpose
```

The /joint_states topic publishes the execution-time robot joint position and velocity values. You can monitor the Robot Joints by subscribing to this topic:
```sh
ros2 topic echo /joint_states
```

### Robot Movements using ROS 2 Actions (/Move & /RobMove)

Robot movements in our ROS 2 Sim-to-Real Robot Control framework are controlled via specific ROS 2 Actions. The two main ROS 2 actions for movement are /Move and /RobMove.

__Move Action__

The /Move action allows you to execute various robot motion commands based on specific movement types and parameters such as speed, joint positions, Cartesian paths, and rotations.

Robot Movements are executed from a single ROS 2 Node in ros2_SimRealRobotControl. A Robot Motion request consists of a simple ROS 2 Action (/Move) call, where the following parameters must be specified:

- The ACTION that is going to be executed.
- The speed at which the robot will execute the action.
- The value of the action to be executed.

Actions can be executed by running the following commands in the Ubuntu Terminal:

__MoveJ__: The Robot moves to the specific waypoint, which is specified by Joint Pose values. (UNIT: m)
```sh
ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveJ', movej: {joint1: 0.00, joint2: 0.00, joint3: 0.00, joint4: 0.00, joint5: 0.00, joint6: 0.00}, speed: 1.0}"
```

__MoveL__: The Robot executes a CARTESIAN/LINEAR path. The End-Effector orientation is kept constant, and the position changes by +-(x,y,z). (UNIT: m)
```sh
ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveL', movel: {x: 0.00, y: 0.00, z: 0.00}, speed: 1.0}"
```

__MoveR__: The Robot rotates the selected joint a specific amount of degrees. (JOINT: jointx, UNIT: deg)
```sh
ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveR', mover: {joint: '--', value: 0.00}, speed: 1.0}"
```

__MoveROT__: The Robot rotates/orientates the End-Effector frame according to the input: EulerAngles(yaw,pitch,roll). THE ROT(yaw,pitch,roll) determines the ADDED ROTATION of the End-Effector, which is applied to the END-EFFECTOR COORDINATE FRAME. (UNIT: def)
```sh
ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveROT', moverot: {yaw: 0.00, pitch: 0.00, roll: 0.00}, speed: 1.0}"
```

__MoveRP__: End-Effector rotation AROUND A POINT -> The Robot rotates/orientates + moves the End-Effector frame according to the input: EulerAngles(yaw,pitch,roll) + Point(x,y,z). THE ROT(yaw,pitch,roll) determines the ADDED ROTATION of the End-Effector, which is applied to the END-EFFECTOR COORDINATE FRAME, AROUND THE (x,y,z) POINT. (UNIT: deg)
```sh
ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveRP', moverp: {x: 0.00, y: 0.00, z: 0.00, yaw: 0.00, pitch: 0.00, roll: 0.00}, speed: 1.0}"
```

__MoveG__: The Gripper fingers move to the specific pose. The "moveg" value is a value between 0-100, representing the gripper opening percentage.
```sh
ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveG', moveg: 0.0, speed: 1.0}"
```

_NOTE: The Robot MOVEMENT SPEED is controlled by the "speed" parameter when executing the specific ROS 2 action. The value must be (0,1]. being 1 the maximum velocity and 0 the null velocity (which is not valid -> A small value must be defined, e.g.: 0.01 represents a very slow movement)._

__RobMove Action__

The /RobMove action is used to move the robot’s end-effector to a specific end-effector pose. It allows for two types of movement:

- PTP (Point-to-Point): The robot moves directly to the target pose via an optimal path in joint space.
- LIN (Linear): The robot moves in a straight line between its current pose and the target pose.

To execute a /RobMove action, the following parameters need to be defined:

- The TYPE of movement: It can be Point-to-Point ("PTP"), or LINEAR ("LIN").
- The speed at which the robot will execute the action.
- The POSE, (POSITION - x,y,z + ROTATION - qx,qy,qz,qw).

/Robmove can be executed by running the following command in the Ubuntu Terminal:
```sh
ros2 action send_goal -f /Robmove ros2srrc_data/action/Robmove "{type: '---', speed: 1.0, x: 0.0, y: 0.0, z: 0.0, qx: 0.0, qy: 0.0, qz: 0.0, qw: 0.0}"
```

_NOTE: The Robot MOVEMENT SPEED is controlled by the "speed" parameter when executing the specific ROS 2 action. The value must be (0,1]. being 1 the maximum velocity and 0 the null velocity (which is not valid -> A small value must be defined, e.g.: 0.01 represents a very slow movement)._

</br>
</br>

---

</br>
</br>

### SOLUTION

1. Launch the ROSConUK26 ABB IRB-120 Robot Cell's Gazebo + MoveIt 2 Simulation Environment:
    ```sh
    ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_2  # IRB-120 + Schunk EGP-64 Gripper.
    ```

2. In 2 different terminal shells, execute the Robot Monitoring ROS 2 Topic Subscribers.
    ```sh
    ros 2 topic echo /joint_states
    ros2 topic echo /Robpose
    ```

3. In a new terminal shell, execute the following movements:
    ```sh
    # MoveJ:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveJ', movej: {joint1: 0.00, joint2: -30.00, joint3: 30.00, joint4: 0.00, joint5: 90.00, joint6: 0.00}, speed: 1.0}"

    # MoveL:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveL', movel: {x: 0.20, y: 0.00, z: 0.0}, speed: 0.1}"

    # MoveL:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveL', movel: {x: 0.00, y: 0.00, z: -0.15}, speed: 0.1}"

    # MoveJ:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveJ', movej: {joint1: 0.00, joint2: 0.00, joint3: 0.00, joint4: 0.00, joint5: 90.00, joint6: 0.00}, speed: 1.0}"

    # MoveR:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveR', mover: {joint: 'joint1', value: 45.00}, speed: 1.0}"

    # MoveR:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveR', mover: {joint: 'joint1', value: -45.00}, speed: 0.25}"

    # MoveROT:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveROT', moverot: {yaw: 0.00, pitch: 0.00, roll: 90.00}, speed: 0.1}"

    # MoveROT:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveROT', moverot: {yaw: 0.00, pitch: 0.00, roll: -90.00}, speed: 1.0}"

    # MoveRP:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveRP', moverp: {x: 0.0, y: 0.00, z: 0.10, yaw: 0.00, pitch: 20.00, roll: 0.0}, speed: 0.25}"

    # MoveRP:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveRP', moverp: {x: 0.0, y: 0.00, z: 0.10, yaw: 0.00, pitch: -40.00, roll: 0.0}, speed: 1.0}"

    # MoveRP:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveRP', moverp: {x: 0.0, y: 0.00, z: 0.10, yaw: 0.00, pitch: 20.00, roll: 0.0}, speed: 0.1}"

    # MoveG:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveG', moveg: 50.0, speed: 1.0}"

    # MoveG:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveG', moveg: 100.0, speed: 1.0}"

    # MoveG:
    ros2 action send_goal -f /Move ros2srrc_data/action/Move "{action: 'MoveG', moveg: 0.0, speed: 1.0}"

    # For RobMove, check the current robot state in /Robpose, and feel free to adjust the xyz,qxqyqzqw values as you wish:
    ros2 action send_goal -f /Robmove ros2srrc_data/action/Robmove "{type: '---', speed: 1.0, x: 0.0, y: 0.0, z: 0.0, qx: 0.0, qy: 0.0, qz: 0.0, qw: 0.0}" # TYPE: PTP or LIN.
    ```