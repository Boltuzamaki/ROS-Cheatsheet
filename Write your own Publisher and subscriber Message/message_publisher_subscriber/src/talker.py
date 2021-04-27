#!/usr/bin/env python
import rospy
print(__name__)
from std_msgs.msg import String
def talker():
    # create a new publisher first specify topic name, then type of messagenthen the queue size
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # we need to initialize the node
    rospy.init_node('talker', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1)
    #keep publishing until Ctrl-C is pressed
    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world "+str(i)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i+=1

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
