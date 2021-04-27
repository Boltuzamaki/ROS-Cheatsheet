#!/usr/bin/env python
import rospy
from message_gen.msg import IOTmessage
import random

def messagepub():
    # create a new publisher first specify topic name, then type of messagenthen the queue size
    pub = rospy.Publisher('messagesub', IOTmessage, queue_size=10)
    # we need to initialize the node
    rospy.init_node('messagepub', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1)
    #keep publishing until Ctrl-C is pressed
    i=0
    while not rospy.is_shutdown():
        iot_mess = IOTmessage()
        iot_mess.id = i
        iot_mess.name = "iot_home"
        iot_mess.temperature = 26 + (random.random()*5)
        iot_mess.humidity =  55 + (random.random()*5)
        rospy.loginfo("I publish: ")
        rospy.loginfo(iot_mess)
        pub.publish(iot_mess)
        rate.sleep()
        i=i+1

if __name__=='__main__':
    try:
        messagepub()
    except rospy.ROSInterruptException:
        pass
