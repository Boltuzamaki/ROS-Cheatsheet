#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def move():
    # create a new publisher. specify the topic name, then type of message the queue size
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # Initialize node
    rospy.init_node('move', anonymous=True)
    # set the loop rate
    rate = rospy.Rate(1)
    # keep publishing until ctrl-C is pressed
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 1.0
        twist.angular.z = 1.0
        speed_publisher.publish(twist)

if __name__ == '__main__':
    try:
        move()
    except:
        pass
