#!/usr/bin/env python3
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
import os
from random import randrange
from bread_gazebo.msg import PusherAction,PusherResult,PusherGoal
import actionlib
from festo.Gantry import Gantry

dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
controller_publisher = rospy.Publisher('pusher_to_controller', UInt32, queue_size=10)
blower_publisher = rospy.Publisher('blower_to_pusher', UInt32, queue_size=1)
component_name = "Pusher Interface"
state = [True]
festo_pusher_ip_address = "10.42.0.100"
festo_pusher_controller = Gantry(festo_pusher_ip_address)

class PusherActionServer(object):
    def __init__(self,driver):
        self._action_name = "PusherAction"
        self._driver = driver
        self._as = actionlib.SimpleActionServer(self._action_name,PusherAction,
            execute_cb=self.execute_cb,auto_start=False)
        self._as.start()
    
    def execute_cb(self,goal):
        if goal.required_status == 1:
            blower_publisher.publish(0)
        self._driver.moveTo(goal.required_status)
        self._feedback = PusherResult(finish_status=goal.required_status)
        if goal.required_status == 0:
            blower_publisher.publish(1)
        rospy.loginfo(self._as)
        self._as.set_succeeded(self._feedback)

def move_to_the_end():
    try:
        festo_pusher_controller.moveTo(1)
        #Publish the finish code.
        controller_publisher.publish(5)
    except RuntimeError:
        #TODO: change to real error code.
        controller_publisher.publish(100)
        raise rospy.ROSInitException("Sealer Controler at " + festo_sealer_ip_address + 
        "has no response, please check the router and network!")

def home():
    try:
        festo_pusher_controller.moveTo(0)
        #process has been finished.
        controller_publisher.publish(2)
    except RuntimeError:
        #TODO: change to real error code.
        controller_publisher.publish(100)
        raise rospy.ROSInitException("Sealer Controler at " + festo_sealer_ip_address + 
        "has no response, please check the router and network!")


def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)

def ctcCallback(data):
    rospy.loginfo("MAMAM MIA %d ",data.data)
    if data.data == 4:
        controller_publisher.publish(2)
    elif data.data == 0:
        state[0] = False
    
def pusher_initialise():
    try:
        #init the controller.
        festo_pusher_controller.enable()
        festo_pusher_controller.home()
    except RuntimeError:
        #TODO: change to real error code.
        festo_pusher_controller.publish(100)
        raise rospy.ROSInitException("Sealer Controler at " + festo_pusher_ip_address + 
        "has no response, please check the router and network!")
    rospy.init_node('pusher_interface', anonymous=False)
    rospy.Subscriber('controller_to_pusher', UInt32, ctcCallback)
    server = PusherActionServer(festo_pusher_controller)
    rospy.spin()

if __name__ == '__main__':
    pusher_initialise()
