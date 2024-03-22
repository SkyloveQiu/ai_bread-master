#!/usr/bin/env python3

from re import I
import threading
from time import sleep
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
from bread_gazebo.srv import BagCheckup,BagCheckupResponse
import os
from bread_gazebo.srv import PollLoaf, PollLoafResponse
from bread_gazebo.srv import BaggingStatus,BaggingStatusResponse
from bread_gazebo.msg import SpinWheelAction, SpinWheelGoal
import actionlib
dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
controller_publisher = rospy.Publisher('bagging_to_controller', UInt32, queue_size=10)
wheel_set_goal = rospy.Publisher('set_goal_wheel', UInt32, queue_size=10)
component_name = "Bagging Interface"
state = [False]
bread_dict = {
  "Tijger Wit": 0,
  "Boulogne": 1,
  "Volkoren Meergranen": 2
}
def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)
def pick_bag(bread_type):
    return
def ctbCallback(data):
    
    if data.data == 1000:
        rospy.wait_for_service('Loaf_Queue_Poll')
        try:
            poll_loaf = rospy.ServiceProxy('Loaf_Queue_Poll', PollLoaf)
            resp = poll_loaf(1)
            wheel_set_goal.publish(bread_dict[resp.breadType])
            #threading.Thread(target=pick_bag,
             #    kwargs={'bread_type':resp.breadType}).start()
            
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
            
    elif data.data == 0:
        state[0] = False
    elif data.data == 5:
        rospy.signal_shutdown("ASYNC CLOSE ISSUED")
        

def demo_check():
    try:
            bag_check = rospy.ServiceProxy('Bag_Check', BagCheckup)
            resp = bag_check(1)
            if resp.responseFlag == 1:
                print("Bag is fine")
            elif resp.responseFlag == 0:
                print("Out of bags")
            elif resp.responseFlag == 2:
                print("Setup")
            else:
                print("Error")
            
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def cleanup():
    rospy.signal_shutdown("SYNC CLOSE ISSUED")
    
def status_ping(req):
    if req.flag == 5:
        
        loop_thread = threading.Thread(target=cleanup)
        loop_thread.setDaemon(True)
        loop_thread.start()
        return BaggingStatusResponse(0, "CLOSING")
def feedback_line(data):
    if data.data == 1:
        try:
            bag_check = rospy.ServiceProxy('Bag_Check', BagCheckup)
            resp = bag_check(1)
            if resp.responseFlag == 1:
                controller_publisher.publish(1)
            elif resp.responseFlag == 0:
                print("Out of bags")
                controller_publisher.publish(911)
            elif resp.responseFlag == 2:
                print("Setup")
            else:
                print("Error")
            
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
        
def baggingInitialise():

   
    
    
    rospy.init_node('bagging_interface', anonymous=False)
    rospy.Subscriber('controller_to_bagging', UInt32, ctbCallback)
    rospy.Subscriber('fw_feedback', UInt32, feedback_line)
    rospy.wait_for_service('Top_Cam_Status')
    rospy.Service('Bagging_Status', BaggingStatus, status_ping)



    rospy.spin()


if __name__ == '__main__':
    baggingInitialise()
