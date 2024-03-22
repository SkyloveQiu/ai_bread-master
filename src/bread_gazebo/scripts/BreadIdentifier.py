#!/usr/bin/env python3
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
import os
from random import randrange

dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
controller_publisher = rospy.Publisher('identifier_to_controller', UInt32, queue_size=10)
component_name = "Bread Identifier"
state = [False]

def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)
        
def ctiCallback(data):
    

    #DEMO ONLY
    if data.data == 1000:
        rate = rospy.Rate(5)
        rate.sleep()
        controller_publisher.publish(1)

        
def identifyBread():
    return randrange(4)
    
def identifierInitialise():

   
    
    
    rospy.init_node('bread_identifier', anonymous=False)
    rospy.Subscriber('controller_to_identifier', UInt32, ctiCallback)

    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()


if __name__ == '__main__':
   identifierInitialise()
