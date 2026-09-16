<!-- 

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

-->

<!--

  README.md TEMPLATE obtined from:
      https://github.com/othneildrew/Best-README-Template
      AUTHOR: OTHNEIL DREW 

-->

<!-- HEADER -->
<br />
<div align="center">

  <a>
    <img src="ROSConUK26 IFRA - Logo.png" alt="header" width="320" height="300">
  </a>

  <br />

  <h2 align="center">Robot Simulation and Control Workshop - ROSCon UK 2026</h2>

  <p align="center">
    IFRA (Intelligent Flexible Robotics and Assembly) Research Group
    <br />
    Centre for Robotics and Assembly
    <br />
    Faculty of Engineering and Applied Sciences (FEAS)
    <br />
    Cranfield University, United Kingdom
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#open-source-tool-for-the-simulation-and-control-of-any-robot-arm-in-ros-2">ROS 2 Workshop Information</a></li>
        <li><a href="#roscon_uk_2026-repository">ROSConUK-2026 GitHub Repository</a></li>
        <li><a href="#intelligent-flexible-robotics-and-assembly-group">IFRA-Cranfield Research Group</a></li>
      </ul>
    </li>
    <li>
      <a href="#documentation">Documentation</a>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#cite-our-work">Cite our work</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br />

<!-- ABOUT THE PROJECT -->
## About

### Open-Source Tool for the Simulation and Control of any Robot Arm in ROS 2

We are excited to welcome you to our hands-on workshop at ROSCon UK 2026, where we will explore a modular, open-source framework for simulating and controlling robot manipulators using ROS 2, MoveIt 2, and Gazebo. The framework is called ros2_SimRealRobotControl (ros2srrc), and is publicly available at https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl.

Developed by the IFRA-Cranfield Research Group at Cranfield University, this framework is designed to streamline the design, deployment, and operation of robotic workcells—whether you are working on industrial robots, collaborative robots, or research prototypes. Our aim is to provide you with a standardised, reusable, and flexible development workflow that supports teaching, research, prototyping, and real-world applications. 

This workshop will be highly practical. You will follow each step alongside us to set up your own ROS 2 environment, run robot simulations, operate a robot arm, and integrate external software tools such as intelligent vision systems and custom Human-Machine Interfaces (HMIs). All resources used in the workshop are fully open-source and will remain available after the session, allowing you to continue experimenting and adapting the framework to your own projects. 

By the end of the workshop, you will: 

- Understand the structure and functionality of our modular ROS 2 framework. 
- Be able to deploy and operate robot workcells in both Gazebo simulation and on real hardware. 
- Know how to integrate external perception and control tools into your ROS 2 workflows. 
- Have a foundation to standardise your robotic development process using reusable packages and launch systems. 

We encourage you to actively participate, ask questions, and share your own insights. The workshop is also a space for discussion on how we can collectively improve and standardise simulation and control practices in ROS 2. 

### ROSCon_UK_2026 Repository

The IFRA-Cranfield/ROSCon_UK_2026 repository contains all the exercises, resources, and example solutions that will be used during the workshop. Having it installed in advance will ensure you can follow each step, replicate demonstrations, and continue experimenting after the session.  

The repository has 3 branches, which means that is available for 3 different ROS 2 environments:

- humble: Ubuntu 22.04, ROS 2 Humble, and Gazebo Classic
- humble_gzfortress: Ubuntu 22.04, ROS 2 Humble, and Gazebo (Ignition) Fortress
- jazzy: Ubuntu 24.04, ROS 2 Jazzy, and Gazebo (Ignition) Harmonic

### Intelligent Flexible Robotics and Assembly Group

The IFRA (Intelligent Flexible Robotics and Assembly) Group is part of the Centre for Robotics and Assembly at Cranfield University.

IFRA Group pushes technical boundaries. At IFRA we provide high tech automation & assembly solutions, and we support smart manufacturing with Smart Industry technologies and solutions. Flexible Manufacturing Systems (FMS) are a clear example. They can improve overall operations and throughput quality by adapting to real-time changes and situations, supporting and pushing the transition towards flexible, intelligent and responsive automation, which we continuously seek and support.

The IFRA Group undertakes innovative research to design, create and improve Intelligent, Responsive and Flexible automation & assembly solutions, and this series of GitHub repositories provide background information and resources of how these developments are supported.

__SOCIAL MEDIA__:

IFRA-Cranfield:
- YouTube: https://www.youtube.com/@IFRACranfield
- LinkedIn: https://www.linkedin.com/in/ifra-cranfield/

Centre for Robotics and Assembly:
- Instagram: https://www.instagram.com/cranfieldrobotics/
- Facebook: https://www.facebook.com/cranfieldunirobotics/
- YouTube: https://www.youtube.com/@CranfieldRobotics
- LinkedIn: https://www.linkedin.com/company/cranfieldrobotics/
- Website: https://www.cranfield.ac.uk/centres/centre-for-robotics-and-assembly 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- DOCUMENTATION -->
## Documentation

__INSTALLATION__: Before the workshop, please make sure you follow the installation instructions, which can be found [here](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/humble/instructions). The repository can be installed and the ROS 2 environment can be reproduced and the tasks executed in 2 different ways:

- By installing ROS 2 Humble, all the required packages and the ROSCon_UK_26 repository on a Ubuntu 22.04 PC.
- By building and running the provided rosconuk26-docker image.

__TASKS__: The instructions to undertake the practical exercises can be found in the [tasks folder](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/humble/tasks).

__SOLUTIONS__: Some of the solutions to the exercises can be found in the [solutions folder](https://github.com/IFRA-Cranfield/ROSCon_UK_2026/tree/humble/solutions), humble-solution branch.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

<p>
  Intelligent Flexible Robotics and Assembly Group
  <br />
  Created on behalf of the IFRA Group at Cranfield University, United Kingdom
  <br />
  E-mail: IFRA@cranfield.ac.uk 
  <br />
  <br />
  Licensed under the Apache-2.0 License.
  <br />
  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
  <br />
  <br />
  <a href="https://www.cranfield.ac.uk/">Cranfield University</a>
  <br />
  Faculty of Engineering and Applied Sciences (FEAS)
  <br />
    <a href="https://www.cranfield.ac.uk/centres/centre-for-robotics-and-assembly">Centre for Robotics and Assembly</a>
  <br />
  College Road, Cranfield
  <br />
  MK43 0AL, Bedfordshire, UK
  <br />
</p>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CITE OUR WORK -->
## Cite our work

<p>
  You can cite our work with the following statements:
  <br />
  IFRA-Cranfield (2023) ROS 2 Sim-to-Real Robot Control. URL: https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl.
  <br />
  IFRA-Cranfield (2026) Robot Simulation and Control Workshop, ROSCon UK 2026. URL: https://github.com/IFRA-Cranfield/ROSCon_UK_2026.
</p>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

<p>
  Mikel Bueno Viso - Research Assistant in Intelligent Automation at Cranfield University
  <br />
  E-mail: Mikel.Bueno-Viso@cranfield.ac.uk
  <br />
  LinkedIn: https://www.linkedin.com/in/mikel-bueno-viso/
  <br />
  Profile: https://www.cranfield.ac.uk/people/mikel-bueno-viso-32884399
  <br />
  <br />
  Dr. Seemal Asif - Lecturer in Artificial Intelligence and Robotics at Cranfield University
  <br />
  E-mail: s.asif@cranfield.ac.uk
  <br />
  LinkedIn: https://www.linkedin.com/in/dr-seemal-asif-ceng-fhea-miet-9370515a/
  <br />
  Profile: https://www.cranfield.ac.uk/people/dr-seemal-asif-695915
  <br />
  <br />
  Professor Phil Webb - Professor of Aero-Structure Design and Assembly at Cranfield University
  <br />
  E-mail: p.f.webb@cranfield.ac.uk
  <br />
  LinkedIn: https://www.linkedin.com/in/phil-webb-64283223/
  <br />
  Profile: https://www.cranfield.ac.uk/people/professor-phil-webb-746415 
  <br />
  <br />
  Naroa Núñez-Calvo - PhD Student and Researcher at Ikerlan S. Coop.
  <br />
  E-mail: nnunez@ikerlan.es
  <br />
  LinkedIn: https://www.linkedin.com/in/naroa-nunez-calvo/
  <br />
  Profile: https://www.ikerlan.es/en/technologies/control-robotics
  <br />
</p>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [README.md template - Othneil Drew](https://github.com/othneildrew/Best-README-Template).
* [ROSCon UK 2026 - Website](https://roscon.org.uk/2026/).


<p align="right">(<a href="#top">back to top</a>)</p>
