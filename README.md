A repository for qut10_jackal.

### Changes from the original state of the robot
- Clearpath suggests using `wicd` to manage the WiFi connection, while we use `nmcli` instead.
- Static IP for the robot on the QUT WiFi: 172.19.54.2
- Make sure to add `172.19.54.2	jackal cpr-qut10.cpr-qut10 cpr-qut10` to your `/etc/hosts/` file
- Enabled Port Forwarding to the ARK as described in Section 4.10 of the ARK user manual; you can reach the ARK with Chrome on http://172.19.54.2
- Corrected time zone: `sudo timedatectl set-timezone Australia/Brisbane`
- Added QUT time server: https://wiki.qut.edu.au/display/cyphy/Our+NTP+server+setting+tutorial

### Install on new machines
- Install jackal related packages: `sudo apt install ros-$ROS_DISTRO-jackal* ros-$ROS_DISTRO-ros-control ros-$ROS_DISTRO-joint-state-controller ros-$ROS_DISTRO-effort-controllers ros-$ROS_DISTRO-position-controllers ros-$ROS_DISTRO-velocity-controllers ros-$ROS_DISTRO-ros-controllers ros-$ROS_DISTRO-gazebo-ros ros-$ROS_DISTRO-gazebo-ros-control`
- Install lcm (requirement for ark_bridge; for some reason the Ubuntu package did not do the job for me)
-- `git clone https://github.com/lcm-proj/lcm.git`
-- `cd lcm && mkdir build && cd build`
-- `ccmake ..`
-- `make && sudo make install`
- Install ark_bridge:
-- `cd ~/catkin_ws/src && git clone https://github.com/autonomyresearchkit/ark_bridge.git`
-- `cd ~/catkin_ws/src/ark_bridge && ./build_client.sh` (at the time of writing, you need to apply the changes in https://github.com/autonomyresearchkit/ark_bridge/pull/1 to get it compiled)
-- `cd ~/catkin_ws/ && catkin build`
