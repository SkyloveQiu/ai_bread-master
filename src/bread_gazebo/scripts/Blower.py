#!/usr/bin/env python3
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
import os
from random import randrange
import Jetson.GPIO as GPIO

dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
component_name = "Blower Interface"
state = [True]
sleep_pin = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sleep_pin,GPIO.OUT)


def emergency():
    GPIO.output(sleep_pin,GPIO.LOW)

def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)

def ctcCallback(data):
    rospy.loginfo("MAMAM MIA %d ",data.data)
    if data.data == 0:
        GPIO.output(sleep_pin,GPIO.HIGH)
    elif data.data == 1:
        GPIO.output(sleep_pin,GPIO.LOW)
    elif data.data == 5:
        rospy.signal_shutdown("ASYNC CLOSE ISSUED")
    elif data.data == 911:
        emergency()

def conveyorInitialise():
    rospy.init_node('conveyor_interface', anonymous=False)
    rospy.Subscriber('blower_to_pusher', UInt32, ctcCallback)
    rospy.spin()

if __name__ == '__main__':
    GPIO.output(sleep_pin,GPIO.LOW)
    conveyorInitialise()
