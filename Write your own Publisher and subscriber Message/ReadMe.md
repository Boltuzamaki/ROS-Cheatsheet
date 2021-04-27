# Getting started with creating message publisher and subscriber for a Topic

![One publisher can send message to many subscriber and one subscriber can get message from multiple publisher](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Write%20your%20own%20Publisher%20and%20subscriber%20Message/Picture/Screenshot%20from%202021-04-27%2003-00-16.png)

![First node which want to subscribe connect to master node](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Write%20your%20own%20Publisher%20and%20subscriber%20Message/Picture/Screenshot%20from%202021-04-27%2003-00-28.png)

![Then node which need to publish connect to master node](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Write%20your%20own%20Publisher%20and%20subscriber%20Message/Picture/Screenshot%20from%202021-04-27%2003-00-30.png)

![Then master send info about publisher node to subsciber node](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Write%20your%20own%20Publisher%20and%20subscriber%20Message/Picture/Screenshot%20from%202021-04-27%2003-00-32.png)

![TCPROS connection established between subscriber and publisher node](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Write%20your%20own%20Publisher%20and%20subscriber%20Message/Picture/Screenshot%20from%202021-04-27%2003-00-36.png)

![Rules for writing Publisher](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Write%20your%20own%20Publisher%20and%20subscriber%20Message/Picture/Screenshot%20from%202021-04-27%2003-00-43.png)

![Rules for writing subscriber](https://github.com/Boltuzamaki/ROS-Cheatsheet/blob/master/Write%20your%20own%20Publisher%20and%20subscriber%20Message/Picture/Screenshot%20from%202021-04-27%2003-00-47.png)

# Create the listner and talker py in your package in src folder
```
cd src_folder_of_project
chmod +x listner.py
chmod +x talker.py
roscore
rosrun your_package_name listner.py
rosrun your_package_name talker.py
```
