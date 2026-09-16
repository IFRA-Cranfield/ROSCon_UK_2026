#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True

# ===================================== COPYRIGHT ===================================== #
#                                                                                       #
#  IFRA (Intelligent Flexible Robotics and Assembly) Group, CRANFIELD UNIVERSITY        #
#  Created on behalf of the IFRA Group at Cranfield University, United Kingdom          #
#  E-mail: IFRA@cranfield.ac.uk                                                         #
#                                                                                       #
#  Licensed under the Apache-2.0 License.                                               #
#  You may not use this file except in compliance with the License.                     #
#  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0  #
#                                                                                       #
#  Unless required by applicable law or agreed to in writing, software distributed      #
#  under the License is distributed on an "as-is" basis, without warranties or          #
#  conditions of any kind, either express or implied. See the License for the specific  #
#  language governing permissions and limitations under the License.                    #
#                                                                                       #
#  IFRA Group - Cranfield University                                                    #
#  AUTHORS: Mikel Bueno Viso - Mikel.Bueno-Viso@cranfield.ac.uk                         #
#           Dr. Seemal Asif  - s.asif@cranfield.ac.uk                                   #
#           Prof. Phil Webb  - p.f.webb@cranfield.ac.uk                                 #
#                                                                                       #
#  Date: October, 2026.                                                                 #
#                                                                                       #
# ===================================== COPYRIGHT ===================================== #

# ======= CITE OUR WORK ======= #
# You can cite our work with the following statements:
# IFRA-Cranfield (2023) ROS 2 Sim-to-Real Robot Control. URL: https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl.
# IFRA-Cranfield (2026) Robot Simulation and Control Workshop, ROSCon UK 2026. URL: https://github.com/IFRA-Cranfield/ROSCon_UK_2026.

# cubePP.py
# This program performs a Cube Pick & Place task.

# ===== IMPORT REQUIRED COMPONENTS ===== #

# System functions and classes:
import sys, os, time

# Required to include ROS2 and its components:
import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory

# IMPORT ROS2 Custom Messages:
from objectpose_msgs.msg import ObjectPose
from ros2srrc_data.msg import Action
from ros2srrc_data.msg import Joint
from ros2srrc_data.msg import Joints
from ros2srrc_data.msg import Xyz
from ros2srrc_data.msg import Xyzypr
from ros2srrc_data.msg import Ypr
from ros2srrc_data.msg import Robpose

# IMPORT Python classes (ros2_SimRealRobotControl Python Clients):
PATH = os.path.join(get_package_share_directory("ros2srrc_execution"), 'python')
PATH_robot = PATH + "/robot"
PATH_endeffector = PATH + "/endeffector"
PATH_endeffector_gz = PATH + "/endeffector_gz"
# ROBOT CLASS:
sys.path.append(PATH_robot)
from robot import RBT
# END EFFECTOR CLASS (Gazebo):
sys.path.append(PATH_endeffector_gz)
from parallelGripper import parallelGR

# ==================================================================== #  
# ==================================================================== # 

# ===== CLOSE PROGRAM function ===== #
def close():

    rclpy.shutdown()
    print("")
    print("CLOSING PROGRAM... BYE!")
    exit()

# ==================================================================== #  
# ==================================================================== # 

def main(args=None):

    rclpy.init()

    print("")
    print(" --- Cranfield University --- ")
    print("        (c) IFRA Group        ")
    print("")
    print(" ROSCon UK 2026 - ROS 2 Robot Simulation and Control Workshop ")
    print("")

    print("Python script -> cubePP.py")
    print("")

 
    # ===== INITIALISE ROBOT AND END-EFFECTOR CLASSES ===== #
    
    # ROBOT:
    ROBOT = RBT()
    # END-EFFECTOR:
    ENDEFFECTOR = parallelGR(["RedCube", "BlueCube", "WhiteCube", "GreenCube"], "irb120", "EE_egp64")

    # ===== CUBE PICK & PLACE TASK ===== #

    '''

        REFERENCES:
        - Move() function call: https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble-gzfortress/ros2srrc_execution/python/testClients/test_Move.py
        - RobMove() function call: https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble-gzfortress/ros2srrc_execution/python/testClients/test_RobMove.py
        - Parallel Gripper - Endeffector() function call: https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/blob/humble-gzfortress/ros2srrc_execution/python/testClients/test_PG.py

        WAYPOINTS:
        - Same as for the cubePP.yaml file.

    '''
    
    # 1. MoveJ to HomePosition:
    print(" ===== [CUBE PP Task]: STEP 1 ===== ")
    print("Moving the IRB120 robot to -> HomePosition...")
    print("")

    # Movement to be added --> ROBOT.Move_EXECUTE() call.

    # 2. PTP-RobMove to PickApproach:
    print(" ===== [CUBE PP Task]: STEP 2 ===== ")
    print("Moving the IRB120 robot to -> PickApproach")
    print("")

    # Movement to be added --> ROBOT.RobMove_EXECUTE() call.

    # 3. LIN-RobMove to Pick:
    print(" ===== [CUBE PP Task]: STEP 3 ===== ")
    print("Moving the IRB120 robot to -> Pick")
    print("")

    # Movement to be added --> ROBOT.RobMove_EXECUTE() call.

    # Small delay before grasping:
    time.sleep(1.0)

    # 4. CLOSE GRIPPER:
    print(" ===== [CUBE PP Task]: STEP 4 ===== ")
    print("Gripper -> CLOSE")
    print("")

    # Movement to be added --> ENDEFFECTOR.CLOSE() call.

    # Small delay after grasping:
    time.sleep(1.0)

    # 5. LIN-RobMove to LiftCube:
    print(" ===== [CUBE PP Task]: STEP 5 ===== ")
    print("Moving the IRB120 robot to -> LiftCube")
    print("")

    # Movement to be added --> ROBOT.RobMove_EXECUTE() call.

    # 6. PTP-RobMove to PlaceApproach:
    print(" ===== [CUBE PP Task]: STEP 6 ===== ")
    print("Moving the IRB120 robot to -> PlaceApproach")
    print("")

    # Movement to be added --> ROBOT.RobMove_EXECUTE() call.

    # 7. LIN-RobMove to Place:
    print(" ===== [CUBE PP Task]: STEP 7 ===== ")
    print("Moving the IRB120 robot to -> Place")
    print("")

    # Movement to be added --> ROBOT.RobMove_EXECUTE() call.

    # Small delay before releasing:
    time.sleep(1.0)

    # 8. OPEN GRIPPER:
    print(" ===== [CUBE PP Task]: STEP 8 ===== ")
    print("Gripper -> OPEN")
    print("")

    # Movement to be added --> ENDEFFECTOR.CLOSE() call.

    # Small delay after releasing:
    time.sleep(1.0)

    # 9. LIN-RobMove to PlaceApproach:
    print(" ===== [CUBE PP Task]: STEP 9 ===== ")
    print("Moving the IRB120 robot to -> PlaceApproach")
    print("")

    # Movement to be added --> ROBOT.RobMove_EXECUTE() call.

    # 10. MoveJ to HomePosition:
    print(" ===== [CUBE PP Task]: STEP 10 ===== ")
    print("Moving the IRB120 robot to -> HomePosition...")
    print("")

    # Movement to be added --> ROBOT.Move_EXECUTE() call.

    # ============================ #

    print("CUBE PICK & PLACE task successfully executed.")
    print("")

    rclpy.shutdown()
    print("CLOSING PROGRAM... BYE!")
    exit()

if __name__ == '__main__':
    main()
