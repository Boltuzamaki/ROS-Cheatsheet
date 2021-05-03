# For turtlesim
```
catkin_create_pkg turtle_cleaner std_msgs rospy roscpp
rosrun turtle_cleaner turtle_cleaner.py
```

# For Turtlebot
```
roscore
# install turtlebot3 date - 03/05/21
sudo apt-get install ros-melodic-turtlebot-*
export TURTLEBOT3_MODEL=burger

roslaunch turtlebot3_gazebo turtlebot3_stage_1.launch
rosrun turtle_cleaner turtle_cleaner.py
```
