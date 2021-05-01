# Getting started with ROS Services

![What is ROS service](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Create%20custom%20ROS%20services/pictures/Screenshot%20from%202021-04-28%2003-36-35.png)

![How ROS Service works](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Create%20custom%20ROS%20services/pictures/Screenshot%20from%202021-04-28%2003-41-10.png)

![ROS Service vs ROS publisher and subscriber](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Create%20custom%20ROS%20services/pictures/Screenshot%20from%202021-04-28%2003-41-13.png)

![Steps for making custom ROS service](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Create%20custom%20ROS%20services/pictures/Screenshot%20from%202021-05-01%2020-38-28.png)

# Service basic cmd code
```
# Show running service
rosservice list
# get info of service
rosservice info /spawn
# get the info of type
rossrv info
# for running service
rosservice call /spawn 9 9 0 t2
```
For creating custom service create a custom folder named srv
And create a file named of service.srv
-----------------------------------------------------------
# Now go to package.xml and add these
```
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>roscpp</build_depend>
  <build_depend>actionlib_msgs</build_depend>
  <build_depend>message_runtime</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_depend>message_generation</build_depend>
  <build_export_depend>roscpp</build_export_depend>
  <build_export_depend>rospy</build_export_depend>
  <build_export_depend>std_msgs</build_export_depend>
  <exec_depend>roscpp</exec_depend>
  <exec_depend>rospy</exec_depend>
  <exec_depend>std_msgs</exec_depend>
  <exec_depend>message_runtime</exec_depend>

```
--------------
# Then go to CmakeLists.txt and add these
```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  actionlib_msgs
)
add_service_files(
   FILES
   AddtwoInteger.srv
 )

 generate_messages(
   DEPENDENCIES
   std_msgs actionlib_msgs
 )

 catkin_package(
   INCLUDE_DIRS include
   LIBRARIES ros_service
   CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
   DEPENDS system_lib
)

 ```
 Now make Cmake file using
 ```
 catkin_make
 ```
Now create a service folder in your package and write server and client code

At last run both server and client py file
```
rosrun ros_service your_serverfile_name.py
rosrun ros_service your_clientfile_name.py
```
