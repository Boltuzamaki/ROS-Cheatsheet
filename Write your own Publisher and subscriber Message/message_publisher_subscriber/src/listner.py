#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # get caller_id: Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "I heard " + data.data)

def listner():
    # initialize node
    rospy.init_node('listner', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    # spin() keeps python existing until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listner()
