#!/usr/bin/env python3
import rospy
from bread_gazebo.srv import BaggingStatus,BaggingStatusResponse
from bread_gazebo.msg import LogMsg, ConveyorMotorAction, ConveyorMotorGoal
from std_msgs.msg import UInt32, Int32
import os

from random import randrange
import Jetson.GPIO as GPIO
# from GPIO_mock import GPIO
import time
import actionlib

dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
controller_publisher = rospy.Publisher('conveyor_to_controller', UInt32, queue_size=10)
motor_control = rospy.Publisher('set_conveyor_goal_pusher', Int32, queue_size=10)
tpcam_publisher = rospy.Publisher('top_cam_input', UInt32, queue_size=10)
component_name = "Conveyor Interface"
conveyor_motor_client = actionlib.SimpleActionClient("conveyor_motor",ConveyorMotorAction)
state = [True]
sleep_pin = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sleep_pin,GPIO.OUT)
#def emergency():
GPIO.output(sleep_pin,GPIO.HIGH)

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
        GPIO.output(sleep_pin,GPIO.LOW)
        # controller_publisher.publish(0)
    elif data.data == 5:
        rospy.signal_shutdown("ASYNC CLOSE ISSUED")

def top_cam_feedback(data):
    if data.data == 0:
        GPIO.output(sleep_pin,GPIO.HIGH)
        goal = ConveyorMotorGoal(moving_steps=1000)
        conveyor_motor_client.send_goal(goal)
        conveyor_motor_client.wait_for_result()
        time.sleep(3)
        
        #ONCE DONE
        controller_publisher.publish(2)
        goal = ConveyorMotorGoal(moving_steps=1000)
        conveyor_motor_client.send_goal(goal)
        conveyor_motor_client.wait_for_result()
        GPIO.output(sleep_pin,GPIO.LOW)
        tpcam_publisher.publish(0)
def cleanup():
    GPIO.cleanup()
    rospy.signal_shutdown("SYNC CLOSE ISSUED")    
def status_ping(req):
    if req.flag == 5:
        
        loop_thread = threading.Thread(target=cleanup)
        loop_thread.setDaemon(True)
        loop_thread.start()
        return BaggingStatusResponse(0, "CLOSING")

def conveyorInitialise():
    rospy.init_node('conveyor_interface', anonymous=False)
    rospy.Subscriber('controller_to_conveyor', UInt32, ctcCallback)
    rospy.Subscriber('top_camera_topic', UInt32, top_cam_feedback)
    conveyor_motor_client.wait_for_server()
    # goal = ConveyorMotorGoal(moving_steps=300)
    # conveyor_motor_client.send_goal(goal)
    # conveyor_motor_client.wait_for_result()
    # goal = ConveyorMotorGoal(moving_steps=-300)
    # conveyor_motor_client.send_goal(goal)
    # conveyor_motor_client.wait_for_result()
    rospy.Service('Conveyor_Status', BaggingStatus, status_ping)
    rospy.spin()

if __name__ == '__main__':
    print("init sleep pin")
    GPIO.output(sleep_pin,GPIO.HIGH)

    conveyorInitialise()
