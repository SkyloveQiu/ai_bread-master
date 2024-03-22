#!/usr/bin/env python3

from __future__ import print_function
import os
import threading
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
from bread_gazebo.srv import EnqueueLoaf,EnqueueLoafResponse
from bread_gazebo.srv import PollLoaf,PollLoafResponse
from bread_gazebo.srv import OverviewQueue,OverviewQueueResponse
from bread_gazebo.srv import LoafStatus,LoafStatusResponse
import rospy


dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)

component_name = "Loaf Queue"
state = [False]
queue = []

def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)

def enqueu_loaf(req):
    print("REQUEST %s\n",req.breadType)
    queue.append(req.breadType)
    return EnqueueLoafResponse(0)
def poll_loaf(req):
    if req.flag != 1:
        return PollLoafResponse(2, "error")
    if len(queue) < 1:
        return PollLoafResponse(1, "Empty Queue") 
    return PollLoafResponse(0, queue.pop())

def overview_queue(req):
    if req.flag != 1:
        return OverviewQueueResponse(2, ["error"])
    return OverviewQueueResponse(0, queue)

    
def cleanup():
    rospy.signal_shutdown("SYNC CLOSE ISSUED")

def status_ping(req):
    if req.flag == 5:
        
        loop_thread = threading.Thread(target=cleanup)
        loop_thread.setDaemon(True)
        loop_thread.start()
        return LoafStatusResponse(0, "CLOSING")

def loaf_queue_server():
    rospy.init_node('Loaf_Queue')
    s = rospy.Service('Loaf_Queue_Enqueue', EnqueueLoaf, enqueu_loaf)
    rospy.Service('Loaf_Queue_Poll', PollLoaf, poll_loaf)
    rospy.Service('Overview_Queue', OverviewQueue, overview_queue)
    rospy.Service('Loaf_Queue_Status', LoafStatus, status_ping)
    rospy.spin()

if __name__ == "__main__":
    loaf_queue_server()