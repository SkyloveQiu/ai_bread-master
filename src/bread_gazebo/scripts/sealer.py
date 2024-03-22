#!/usr/bin/env python3
from contextlib import contextmanager
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
import os
from random import randrange
from festo.Gantry import Gantry
import actionlib
from bread_gazebo.msg import SealerAction,SealerResult,SealerGoal
import time

dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
controller_publisher = rospy.Publisher('sealer_to_controller', UInt32, queue_size=10)
component_name = "Sealer Interface"
state = [True]
festo_sealer_ip_address = "10.42.0.101"
festo_sealer_controller = Gantry(festo_sealer_ip_address)

class SealerActionServer(object):
    def __init__(self, driver):
        self._action_name = "SealerAction"
        self._driver = driver
        self._as = actionlib.SimpleActionServer(self._action_name,SealerAction,
            execute_cb=self.run)
        self._as.start()
        
    def run(self,goal):
        print(goal.required_status)
        self._driver.moveTo(goal.required_status)
        self._feedback = SealerResult(finish_status=goal.required_status)
        self._as.set_succeeded(self._feedback)
  



def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)

def ctcCallback(data):
    rospy.loginfo("MAMAM MIA %d ",data.data)
    if data.data == 0:
        pass
        #move_to_the_end()
    elif data.data == 1:
        #home()        
        pass

# def move_to_the_end():
#     try:
#         festo_sealer_controller.moveTo(1)
#         #Publish the finish code.
#         controller_publisher.publish(5)
#     except RuntimeError:
#         #TODO: change to real error code.
#         controller_publisher.publish(100)
#         raise rospy.ROSInitException("Sealer Controler at " + festo_sealer_ip_address + 
#         "has no response, please check the router and network!")

# def home():
#     try:
#         festo_sealer_controller.moveTo(0)
#         #process has been finished.
#         controller_publisher.publish(2)
#     except RuntimeError:
#         #TODO: change to real error code.
#         controller_publisher.publish(100)
#         raise rospy.ROSInitException("Sealer Controler at " + festo_sealer_ip_address + 
#         "has no response, please check the router and network!")

def sealer_initialise():
    global festo_sealer_controller
    try:
        #init the controller.
        festo_sealer_controller.enable()
        festo_sealer_controller.home()
        print("home finished.")
    except RuntimeError:
        #TODO: change to real error code.
        controller_publisher.publish(100)
        raise rospy.ROSInitException("Sealer Controler at " + festo_sealer_ip_address + 
        "has no response, please check the router and network!")
    rospy.init_node('sealer_interface', anonymous=False)
    SealerActionServer(festo_sealer_controller)
    rospy.loginfo("Sealer homing ready")
    rospy.Subscriber('controller_to_sealer', UInt32, ctcCallback)
    print("starting seal")
    # sealer_client = actionlib.SimpleActionClient("Sealer",SealerAction)
    # print("wait server")
    # sealer_client.wait_for_server()
    # print("send goal")
    # goal = SealerGoal(required_status=1)
    # sealer_client.send_goal(goal)
    # sealer_client.wait_for_result()
    # sealer_client.get_result()
    rospy.spin()

if __name__ == '__main__':
    sealer_initialise()
