#!/usr/bin/env python

from ros_service.srv import AddtwoInteger
from ros_service.srv import AddtwoIntegerRequest
from ros_service.srv import AddtwoIntegerResponse

import rospy

def handle_add_to_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a+req.b)))
    return AddtwoIntegerResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddtwoInteger, handle_add_to_ints)
    print("Ready to add two ints")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
