#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
yaw = 0

def poseCallback(pose_message):
    global x
    global y, z, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(speed, distance, is_forward):
    # declear a Twist message to send velocity commands
    velocity_message = Twist()
    # get current location
    global x,y
    x0 = x
    y0 = y

    if(is_forward):
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    distance_moved = 0.0
    loop_rate = rospy.Rate(10) # Publish at a rate of 10 times a second
    cmd_vel_topic = '/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    t0 = rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("Turtlebot moves forwards")
        t1 = rospy.Time.now().to_sec()
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        distance_moved = (t1-t0)*speed
        print(distance_moved)
        if not (distance_moved < distance):
            rospy.loginfo("reached")
            break
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)


def rotate(angular_speed_degree, relative_angle_degree, clockwise):
    global yaw
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0

    #get current location
    theta0 = yaw
    angular_speed = math.radians(abs(angular_speed_degree))

    if(clockwise):
        velocity_message.angular.z = -abs(angular_speed)
    else:
        velocity_message.angular.z = abs(angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10)
    cmd_vel_topic = '/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    t0 = rospy.Time.now().to_sec()

    while True:

        rospy.loginfo("Turtlebot roatate")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        print(current_angle_degree)
        loop_rate.sleep()

        if (current_angle_degree > relative_angle_degree):
            rospy.loginfo("reached")
            break
        #Stop the bot
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)

if __name__ == "__main__":
    try:
        rospy.init_node('turtlebot_motion_pose', anonymous=True)

        # declear velocity publisher
        cmd_vel_topic = '/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)


        move(1.0, 2.0, False)
        rotate(30, 60, True)


    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
