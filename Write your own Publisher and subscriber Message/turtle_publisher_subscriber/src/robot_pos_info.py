#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(data):
    # get caller_id: Get fully resolved name of local node
    rospy.loginfo('x : '+str(data.linear.x)+ ' y :'+str(data.linear.y)+"\n"+'zw :'+str(data.angular.z))

def poslistner():
    # initialize node
    rospy.init_node('poslistner', anonymous=True)

    rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)

    # spin() keeps python existing until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    poslistner()
