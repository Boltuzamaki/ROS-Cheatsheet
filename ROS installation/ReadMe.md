# Install ROS melodic

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -

sudo apt update

sudo apt install ros-melodic-desktop-full

sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

sudo apt install python-rosdep

sudo rosdep init

rosdep update
```

# Setting up Workspace
```
cd ~

gedit .bashrc

# add to bashrc
source /opt/ros/melodic/setup.bash
```
restart terminal

```
roscd
roscore
```
The above command should be working in terminal
Now type
```
mkdir -p ~/catkin`_ws/src

cd catkin_ws/

catkin_make

source ./devel/setup.bash
```
# Create Package
```
cd ~/catkin_ws/src

catkin_create_pkg ros_basic std_msgs rospy roscpp

cd ..

catkin_make
```

