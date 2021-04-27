#!/usr/bin/env python
import rospy
from message_gen.msg import IOTmessage

def callback(data):
    # get caller_id: Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "Info :" + "\n" + "id : "+str(data.id) \
                  +"\n"+ "name : "+str(data.name)+"\n" \
                  "temperature : "+str(data.temperature)+ "\n" \
                  "humidity : "+ str(data.humidity))

def listner():
    # initialize node
    rospy.init_node('listner', anonymous=True)

    rospy.Subscriber('messagesub', IOTmessage, callback)

    # spin() keeps python existing until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listner()
