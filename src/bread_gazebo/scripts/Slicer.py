#!/usr/bin/env python3
import threading
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
import os
import Jetson.GPIO as GPIO
from random import randrange
import time
from bread_gazebo.srv import SlicerStatus,SlicerStatusResponse
dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
emergency_publisher = rospy.Publisher('emergency_signal', UInt32, queue_size=1)
controller_publisher = rospy.Publisher('slicer_to_controller', UInt32, queue_size=10)
component_name = "Slicing Interface"
state = [False]
slicer_start = 37
slicer_stop = 36
current_status = 0
# init the GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup([slicer_start,slicer_stop], GPIO.OUT)
GPIO.output([slicer_stop],GPIO.HIGH)

def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)
        
'''
    Start Code : 100
    Stop Code ： 101
    Reset Code : 102
    Emergency Code : 103
    Reset Emergency : 104
'''

def ctsCallback(data):
    print(data.data)
    global current_status
    #DEMO ONLY:
    if data.data == 1:
        state[0] = True
    if data.data == 100:
        print("starting")
        start_up()
        controller_publisher.publish(1)
    if data.data == 101:
        stop()
    if data.data == 102:
        reset()
    if data.data == 103:
        emergency_stop()
    if data.data == 104:
        emergency_reset()
    if data.data == 1000:
        if state[0]:
            if(hand_detected()):
                sendToLog(1, "HAND DETECTED NEAR BLADES")
                controller_publisher.publish(5)
                state[0] = False
            else:
                controller_publisher.publish(1000)
    elif data.data == 5:
        rospy.signal_shutdown("ASYNC CLOSE ISSUED")

#function for start up.
def start_up():
    global current_status
    if current_status != 0:
        #reset the machine to opration position
        raise rospy.exceptions.ROSException("The machine is not under operation status!") 
    GPIO.output(slicer_stop,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(slicer_stop,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(slicer_stop,GPIO.HIGH)
    GPIO.output(slicer_start,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(slicer_start,GPIO.LOW)
    time.sleep(10)
    GPIO.output(slicer_start,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(slicer_start,GPIO.LOW)
    time.sleep(9)
    GPIO.output(slicer_stop,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(slicer_stop,GPIO.LOW)
    print("starting")
def hand_detected():
    return randrange(6) == 3
def cleanup():
    rospy.signal_shutdown("SYNC CLOSE ISSUED")
    
def status_ping(req):
    if req.flag == 5:
        
        loop_thread = threading.Thread(target=cleanup)
        loop_thread.setDaemon(True)
        loop_thread.start()
        return SlicerStatusResponse(0, "CLOSING")


#stop the machine
def stop():
    global current_status
    GPIO.output(slicer_stop,GPIO.LOW)
    current_status = 1
    time.sleep(0.1)
    GPIO.output(slicer_stop,GPIO.HIGH)

#reset the slicer to standard operation position
def reset():
    global current_status
    if current_status != 1:
        raise rospy.exceptions.ROSException("The machine is not under stop status!") 
    GPIO.output(slicer_start,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(slicer_start,GPIO.LOW)
    current_status = 0

#reset the emergency button
def emergency_reset():
    global current_status
    if current_status != 2:
        raise rospy.exceptions.ROSException("The machine is not under emergency stop status!") 
    GPIO.output(slicer_start,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(slicer_start,GPIO.LOW)
    
#output the emergency button status, 0 means normal, 1 means emergency button pressed.
#When rising means the button is released, output 0.
#when falling means the button is pressed, output 1.
def slicerInitialise():
    rospy.init_node('slicer_interface', anonymous=False)
    rospy.Subscriber('controller_to_slicer', UInt32, ctsCallback)
    #add event, checking rate can be changed by add param bouncetime. Detailed documetation can be found on https://github.com/NVIDIA/jetson-gpio.
    rospy.Service('Slicer_Status', SlicerStatus, status_ping)

    rospy.spin()


if __name__ == '__main__':
    slicerInitialise()
