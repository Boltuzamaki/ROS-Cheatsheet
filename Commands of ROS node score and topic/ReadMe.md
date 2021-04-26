# Commands of ROS node and topic

```
# starts ROS server Master node it is necessary to run below codes
roscore

# list all rosnode
rosnode list

# list all rostopic
rostopic list

# Run the ROS node
rosrun turtlesim # just running this tells the all nodes present in turtlesim

rosrun turtlesim turtlesim_node # Runs turtlesim node

# Get info of a programme ie list all services/nodes/topics

rosnode info /turtlesim

# get info about a topic
rostopic info /turtle1/cmd_vel

# Show info about a message sent by topic
rosmsg show geometry_msgs/Twist

# Run key control programme of turtle sim
rosrun turtlesim turtle_teleop_key

# Get value of topic in real time
rostopic echo /turtle1/cmd_vel

# Feed topic messsage via terminal
rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'

# Change default python to python3
alias python=python3

source ~/.bashrc

pip3 install rospkg


# See the real time graph of whats running
rosrun rqt_graph rqt_graph
```
