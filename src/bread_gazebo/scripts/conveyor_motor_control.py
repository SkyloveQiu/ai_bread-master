#!/usr/bin/env python3
import time
import math
import Jetson.GPIO as GPIO
import rospy
from bread_gazebo.msg import LogMsg, ConveyorMotorAction, ConveyorMotorResult, ConveyorMotorFeedback
from std_msgs.msg import Float32, UInt32, Int32
from pid.PID import pid1, pid2
from threading import Thread
import actionlib
# topic command
# rostopic pub /ferris_wheel_control std_msgs/Float32 3
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
component_name = "Pusher Interface"
enabled = True
enable_passive = True
enable_pin = 26
dir_pin = 23
step_pin = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup([enable_pin,dir_pin,step_pin], GPIO.OUT)
class ConveyorMotorActionServer(object):
    def __init__(self):
        self.__action_name = "conveyor_motor"
        self.__as = actionlib.SimpleActionServer(self.__action_name, ConveyorMotorAction,
                                                    execute_cb=self.run,auto_start=False)
        self.__as.start()

    def run(self,goal):
        print(goal.moving_steps)
        if goal.moving_steps >0:
            GPIO.output(dir_pin, GPIO.HIGH)
        elif goal.moving_steps <0:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaAA")
            GPIO.output(dir_pin, GPIO.LOW)
        steps_needed = goal.moving_steps
        for i in range (steps_needed):
            GPIO.output(step_pin, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(step_pin, GPIO.LOW)
            time.sleep(0.001)
            feedback = ConveyorMotorFeedback(current_moved_steps=i)
            self.__as.publish_feedback(feedback)
        self.__as.set_succeeded()

def sendToLog(type, msg):
    data = LogMsg()
    data.type = type
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)
    
        
def shutdown_routine():

    GPIO.cleanup()

# TODO: Check if one of the threads has died
def ferris_control_initialise():
    rospy.init_node('pusher_controller', anonymous=False)
    rospy.on_shutdown(shutdown_routine)

    server = ConveyorMotorActionServer()
    rospy.spin()



if __name__ == '__main__':
    GPIO.output(enable_pin, GPIO.LOW)
    print("init with high")
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)
    ferris_control_initialise()