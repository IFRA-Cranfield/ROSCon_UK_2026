# Installation - Docker

This workshop is based on [ros2_SimRealRobotControl (ros2srrc)](https://github.com/IFRA-Cranfield/ros2_SimRealRobotControl/tree/jazzy), an open-source framework developed by the IFRA-Cranfield Research Group at Cranfield University. This installation uses Docker to create an **Ubuntu 24.04 environment with ROS 2 Jazzy, Gazebo Harmonic, ROS 2 Control, MoveIt 2 and ros2srrc**, together with the robot drivers and computer vision libraries required for the workshop.

The software is installed and built inside a Docker image. You do not need to install ROS 2 or Gazebo on your computer directly. When you start a container from this image, you can run the workshop commands inside it and display Gazebo and RViz on your Ubuntu desktop.

This guide uses **development mode**: you edit the workshop repository on your computer and make those files available inside the container. This allows you to complete the exercises without rebuilding the entire Docker image after each change.

The requirements are:

- **An Ubuntu desktop computer with a 64-bit Intel or AMD processor.** The host does not have to run Ubuntu 24.04; Ubuntu 22.04 can also host the Ubuntu 24.04 container. Use a release supported by [Docker Engine for Ubuntu](https://docs.docker.com/engine/install/ubuntu/#os-requirements).
- **Docker Engine**, installed in Part A, and access to `sudo`.
- **A graphical desktop session** for Gazebo and RViz. The execution commands below use X11; an **Ubuntu on Xorg** login session is the most straightforward option.
- **An internet connection and sufficient free disk space** for the base image, dependencies and compiled workspace. Allow several tens of GB of free space for the image and build cache.

Docker is also available on other operating systems, but the display and networking commands in this guide target **Docker Engine running directly on Ubuntu**. Windows, macOS and Docker Desktop require different host integration steps.

The procedure is divided into three parts, followed by the execution instructions:

- **Part A:** Install Docker Engine and the host tools.
- **Part B:** Download the workshop repository.
- **Part C:** Build the workshop image.
- **Execution Instructions:** Start the development container, launch the simulation and rebuild your workshop changes.

**Terminal convention:** Commands marked **HOST** run in your normal Ubuntu terminal. Commands marked **CONTAINER** run in a terminal opened inside the Docker container.

## PART A: Install Docker

This section installs Docker Engine using its official Ubuntu package repository ([REF: Docker Engine installation](https://docs.docker.com/engine/install/ubuntu/#install-using-the-apt-repository)). If Docker already works with `sudo docker run --rm hello-world`, complete step 1 and continue to Part B. For an existing installation with conflicting packages, follow the official guide's uninstall instructions before changing package sources.

1. Install the host tools:

    ```sh
    # HOST:
    sudo apt update
    sudo apt install -y ca-certificates curl git x11-xserver-utils
    ```

2. Add Docker's signing key and package repository:

    ```sh
    # HOST: Add the signing key.
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # HOST: Configure the repository for your Ubuntu release.
    sudo tee /etc/apt/sources.list.d/docker.sources > /dev/null <<EOF
    Types: deb
    URIs: https://download.docker.com/linux/ubuntu
    Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
    Components: stable
    Architectures: $(dpkg --print-architecture)
    Signed-By: /etc/apt/keyrings/docker.asc
    EOF
    ```

3. Install and start Docker Engine:

    ```sh
    # HOST:
    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo systemctl enable --now docker
    ```

4. Verify the installation:

    ```sh
    # HOST:
    sudo docker run --rm hello-world
    ```

    You should see the message **Hello from Docker!**. The commands below use `sudo`, so changing your user groups is unnecessary.

## PART B: Clone the ROSCon_UK_2026 Repository

The local repository contains the [Dockerfile](../docker/Dockerfile), the `rosconuk26` ROS 2 package, the workshop tasks and their solutions. Keep this checkout on your computer so you can edit the exercise files with your usual editor.

5. Download the **jazzy** branch:

    ```sh
    # HOST:
    mkdir -p ~/dev_ws/src
    cd ~/dev_ws/src
    git clone -b jazzy https://github.com/IFRA-Cranfield/ROSCon_UK_2026.git
    ```

## PART C: Build the Docker Image

The Dockerfile installs the workshop dependencies, downloads the supporting repositories and builds the ROS 2 workspace at `/dev_ws`. It also configures the ROS environment for interactive Bash terminals.

6. Build the image from the repository root:

    ```sh
    # HOST:
    cd ~/dev_ws/src/ROSCon_UK_2026
    sudo docker build -f docker/Dockerfile -t rosconuk26:jazzy .
    ```

    The final `.` selects the current directory as the build context, including the local workshop files. The name `rosconuk26:jazzy` identifies the resulting image. Wait for the build to finish successfully before starting a container.

    The first build downloads and compiles the environment and can take some time. Subsequent builds reuse completed steps where possible. For more detailed build output, add `--progress=plain` to the command.

7. Check that the image is available:

    ```sh
    # HOST:
    sudo docker image ls rosconuk26:jazzy
    ```

## Execution Instructions

The following steps create a named container, `rosconuk26-docker`, and connect your local repository to `/dev_ws/src/ROSCon_UK_2026` inside it using a [Docker bind mount](https://docs.docker.com/engine/storage/bind-mounts/). Only the workshop repository is mounted; the supporting packages and compiled workspace remain inside the container.

8. Enable access to your desktop display:

    ```sh
    # HOST: Run from a terminal in your Ubuntu desktop session, without sudo.
    echo "$DISPLAY"
    xhost +si:localuser:root
    ```

    `DISPLAY` should contain a value such as `:0` or `:1`. The `xhost` command allows the container's root user to connect to your X display. If the value is empty, use a terminal in your graphical desktop session. If your Wayland session cannot display the applications through XWayland, log out and select **Ubuntu on Xorg** from the login screen's session menu, where available.

9. Create and enter the development container:

    ```sh
    # HOST:
    cd ~/dev_ws/src/ROSCon_UK_2026
    sudo docker run -it \
        --name rosconuk26-docker \
        --network host \
        --shm-size=512m \
        --env DISPLAY="$DISPLAY" \
        --env QT_X11_NO_MITSHM=1 \
        --env QT_QPA_PLATFORM=xcb \
        --device /dev/dri \
        --group-add video \
        --mount type=bind,source=/tmp/.X11-unix,target=/tmp/.X11-unix,readonly \
        --mount "type=bind,source=$(pwd),target=/dev_ws/src/ROSCon_UK_2026" \
        --workdir /dev_ws \
        rosconuk26:jazzy \
        bash
    ```
    
    You are now inside the container. The image automatically sources ROS 2 Jazzy and `/dev_ws/install/local_setup.bash` when an interactive Bash terminal opens.

10. Build the current workshop files and check the environment:

    ```sh
    # CONTAINER:
    cd /dev_ws
    colcon build --packages-select rosconuk26
    source /dev_ws/install/local_setup.bash

    # CONTAINER: Verify the ROS distribution and workshop package:
    echo "$ROS_DISTRO"
    ros2 pkg prefix rosconuk26
    ```

    The expected results are `jazzy` and `/dev_ws/install/rosconuk26`. This rebuild ensures the installed package matches the local checkout mounted into the container, including changes made since the image was built.

11. Launch a workshop robot cell with Gazebo and MoveIt 2:

    ```sh
    # CONTAINER: Launch ROS 2 Environment -> ABB IRB-120 with the Schunk EGP-64 gripper:
    ros2 launch ros2srrc_launch moveit2.launch.py package:=rosconuk26 config:=rosconuk26_2
    ```

    Gazebo and RViz should open on your desktop. Keep this terminal running while using the robot.

12. Open additional terminals for the workshop exercises:

    ```sh
    # HOST: Run in a new Ubuntu terminal for each additional container shell.
    sudo docker exec -it rosconuk26-docker bash
    ```

    Run the task commands in these container terminals. For example, while the simulation is running:

    ```sh
    # CONTAINER:
    ros2 topic list
    ```

    Each `docker exec` terminal joins the same running container. Continue with the exercises in the [tasks folder](../tasks).

13. Edit and rebuild workshop files in development mode:

    Open `~/dev_ws/src/ROSCon_UK_2026` in your editor **on the host** and make the changes requested in the exercises. The mounted source files update immediately inside the container. The package installs copies of its resources and scripts, so rebuild it after edits before relaunching the affected programs:

    ```sh
    # CONTAINER: Stop the affected launch/program with Ctrl+C before rebuilding.
    cd /dev_ws
    colcon build --packages-select rosconuk26
    source /dev_ws/install/local_setup.bash
    ```

    Source the workspace in any other open container terminal before using newly added executables. Build outputs stay in `/dev_ws/build`, `/dev_ws/install` and `/dev_ws/log` inside the container. Edit source files on the host to retain your normal file ownership; files created through the mount by the container's root user are owned by root on the host.

    Rebuild the Docker image when you change its installed dependencies or the Dockerfile. Ordinary workshop source edits only require the package rebuild above.

14. Stop and resume your container:

    Stop running ROS launch files with **Ctrl+C**. To stop the entire container, run:

    ```sh
    # HOST:
    sudo docker stop rosconuk26-docker

    # Revoke display access when finished:
    xhost -si:localuser:root
    ```

    To resume it later from the same desktop display:

    ```sh
    # HOST:
    xhost +si:localuser:root
    sudo docker start -ai rosconuk26-docker
    ```

    Use `sudo docker exec -it rosconuk26-docker bash` for additional terminals once it is running. To inspect its status:

    ```sh
    # HOST:
    sudo docker ps -a --filter name=rosconuk26-docker
    ```

    **(EXTRA) -> Recreate the container after rebuilding the image:** Existing containers keep their original image. Stop and remove the old container, then repeat steps 8–10:

    ```sh
    # HOST:
    sudo docker stop rosconuk26-docker
    sudo docker rm rosconuk26-docker
    ```

    Removing the container deletes its internal builds and any files saved only inside it. Your mounted workshop checkout remains on the host. Also recreate the container if the host checkout moves or your `DISPLAY` value changes, because the mount path and display setting are fixed when the container is created.

_EXTRA ->_ Use the NVIDIA GPU to render the simulation environment and run the tasks inside Docker:

```sh
# HOST - Install nvidia-container-toolkit:
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# HOST - Run the Docker image using the following command:
cd ~/dev_ws/src/ROSCon_UK_2026
sudo docker run -it \
    --name rosconuk26-docker \
    --network host \
    --ipc=host \
    --shm-size=2g \
    --gpus all \
    --env NVIDIA_VISIBLE_DEVICES=all \
    --env NVIDIA_DRIVER_CAPABILITIES=graphics,compute,utility,display \
    --env DISPLAY="$DISPLAY" \
    --env QT_X11_NO_MITSHM=1 \
    --env QT_QPA_PLATFORM=xcb \
    --device /dev/dri \
    --group-add video \
    --mount type=bind,source=/tmp/.X11-unix,target=/tmp/.X11-unix,readonly \
    --mount "type=bind,source=$(pwd),target=/dev_ws/src/ROSCon_UK_2026" \
    --workdir /dev_ws \
    rosconuk26:jazzy \
    bash
```
