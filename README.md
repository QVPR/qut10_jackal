A repository for qut10_jackal.

### Changes from the original state of the robot
- Clearpath suggests using `wicd` to manage the WiFi connection, while we use `wpa_supplicant` in `/etc/network/interfaces` directly instead.
- Static IP for the robot on the QUT WiFi: 172.19.54.2
- Enabled Port Forwarding to the ARK as described in Section 4.10 of the ARK user manual; you can reach the ARK with Chrome on http://172.19.54.2
- Corrected time zone: `sudo timedatectl set-timezone Australia/Brisbane`
- Added QUT time server: https://wiki.qut.edu.au/display/cyphy/Our+NTP+server+setting+tutorial
- Set `magnetic_declination_radians: 0.1923` in `/etc/ros/melodic/ros.d/navsat.launch`
- Let ntpdate wait for network to be up: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=766838#20
- Disable ipv6 in GRUB: https://www.configserverfirewall.com/ubuntu-linux/ubuntu-disable-ipv6/

### Setting up a new robot
- ros.d contains custom scripts that are running at startup through the ROS service setup by clearpath. This should be put in /etc/ros/melodic/ros.d when setting up the robot.
- clearpath_scripts contains executables that Clearpath places in /usr/sbin by default
- clearpath_services contains service files that Clearpath places in /etc/systemd/system by default

### Install on new machines
- Install jackal related packages: `sudo apt install ros-$ROS_DISTRO-jackal* ros-$ROS_DISTRO-ros-control ros-$ROS_DISTRO-joint-state-controller ros-$ROS_DISTRO-effort-controllers ros-$ROS_DISTRO-position-controllers ros-$ROS_DISTRO-velocity-controllers ros-$ROS_DISTRO-ros-controllers ros-$ROS_DISTRO-gazebo-ros ros-$ROS_DISTRO-gazebo-ros-control`
- Make sure to add `172.19.54.2	jackal cpr-qut10.cpr-qut10 cpr-qut10` to your `/etc/hosts/` file
- Add `export ROS_IP=$(hostname -I | awk '{print $1}')` and `export ROS_MASTER_URI=http://jackal:11311` to your `.bashrc`
- Optional:
  - Install lcm (requirement for ark_bridge; for some reason the Ubuntu package did not do the job for me)
    - `git clone https://github.com/lcm-proj/lcm.git`
    - `cd lcm && mkdir build && cd build`
    - `ccmake ..`
    - `make && sudo make install`
  - Install ark_bridge:
    - `cd ~/catkin_ws/src && git clone https://github.com/autonomyresearchkit/ark_bridge.git`
    - `cd ~/catkin_ws/src/ark_bridge && ./build_client.sh` (at the time of writing, you need to apply the changes in https://github.com/autonomyresearchkit/ark_bridge/pull/1 to get it compiled)
    - `cd ~/catkin_ws/ && catkin build`
