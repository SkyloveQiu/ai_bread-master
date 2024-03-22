#!/usr/bin/env python3
from posixpath import join
import Jetson.GPIO as GPIO
import rospy
from bread_gazebo.msg import LogMsg, UserMsg, PusherAction, SealerAction, ConveyorAction, PusherGoal, SealerGoal, ConveyorGoal,TfResult
from std_msgs.msg import UInt32
import os
from bread_gazebo.srv import EnqueueLoaf, EnqueueLoafResponse
from bread_gazebo.srv import LoafStatus,LoafStatusResponse
from bread_gazebo.srv import BaggingStatus,BaggingStatusResponse
from bread_gazebo.srv import SlicerStatus,SlicerStatusResponse
from bread_gazebo.srv import UserStatus,UserStatusResponse
import actionlib
component_name = "Controller"
dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
user_publisher = rospy.Publisher('controller_to_user', UserMsg, queue_size=10)
bag_publisher = rospy.Publisher('controller_to_bagging', UInt32, queue_size=10)
conveyor_publisher = rospy.Publisher('controller_to_conveyor', UInt32, queue_size=10)
slicer_publisher = rospy.Publisher('controller_to_slicer', UInt32, queue_size=10)
detector_publisher = rospy.Publisher('controller_to_detector', UInt32, queue_size=1)
identifier_publisher = rospy.Publisher('controller_to_identifier', UInt32, queue_size=1)
pin_caps = 15
bread_queue = []
state = [False, True]
pusher_client = actionlib.SimpleActionClient("PusherAction",PusherAction)
sealer_client = actionlib.SimpleActionClient("SealerAction",SealerAction)
emergency_in = 38
emergency_out = 40
leds_1 = 21
# leds_2 = 23
GPIO.setmode(GPIO.BOARD)
GPIO.setup(emergency_in,GPIO.IN)
GPIO.setup(emergency_out,GPIO.OUT)
GPIO.setup(leds_1,GPIO.OUT)
# GPIO.setup(leds_2,GPIO.OUT)
GPIO.output(leds_1, GPIO.HIGH)
# GPIO.output(leds_2, GPIO.HIGH)
GPIO.setup(pin_caps, GPIO.IN)
GPIO.output(emergency_out, GPIO.HIGH)
sync_flag_slicer = False
sync_flag_bagging = False
sync_flag_id = False
count_queue = 0
class Controller_State(object):
    def __init__(self) -> None:
        self.errors = False
        self.conveyor = True
        self.ui = True
        self.bagging = True
        self.slicer = True
        self.identifier = True
        self.queue = True
        self.on = False
        self.em = False
        super().__init__()


state_c = Controller_State()
def shutdown_routine():
    if state_c.ui:
        try:
            req = rospy.ServiceProxy('User_Status', UserStatus)
            resp = req(5)
            if resp.responseFlag == 0:
                state_c.ui = False
        except rospy.ServiceException as e:
            sendToLog(2,"TRYING ASYNC CLOSE OF USER")
            sendToUser(5)
            print("COULD NOT CONNECT TO emergency_in = 38,SERVICE (ASSUMING DOWN): %s"%e)
    
    if state_c.conveyor:
        conveyor_publisher.publish(5)

    
    if state_c.bagging:
        try:
            req = rospy.ServiceProxy('Bagging_Status', BaggingStatus)
            resp = req(5)
            if resp.responseFlag == 0:
                state_c.bagging = False
        except rospy.ServiceException as e:
            sendToLog(2,"TRYING ASYNC CLOSE OF BAGGING")
            bag_publisher.publish(5)
            print("COULD NOT CONNECT TO SERVICE (ASSUMING DOWN): %s"%e)

    if state_c.slicer:
        try:
            req = rospy.ServiceProxy('Slicer_Status', SlicerStatus)
            resp = req(5)
            if resp.responseFlag == 0:
                state_c.slicer = False
        except rospy.ServiceException as e:
            sendToLog(2,"TRYING ASYNC CLOSE OF SLICER")
            slicer_publisher.publish(5)
            print("COULD NOT CONNECT TO SERVICE (ASSUMING DOWN): %s"%e)

    if state_c.queue:
        try:
            req = rospy.ServiceProxy('Loaf_Queue_Status', LoafStatus)
            resp = req(5)
            if resp.responseFlag == 0:
                state_c.queue = False
        except rospy.ServiceException as e:
            sendToLog(2,"ASSUMING LOAF QUEUE IS DOWN (NO RESPONSE TO SERVICE CALL)")
            print("COULD NOT CONNECT TO SERVICE (ASSUMING DOWN): %s"%e)
    sendToLog(5,"CLOSING")

    # CLEAR GPIOS
    GPIO.cleanup()
    return 0

def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)
        
def btcCallback(data):
    global sync_flag_slicer
    global sync_flag_id
    global sync_flag_bagging
    if data.data==1:
        if sync_flag_slicer:
            sync_flag_bagging = False
            sync_flag_id = False
            sync_flag_slicer=False
            # start fan and pusher
            result_pusher = push_pusher()
            result_sealer = push_sealer()
            if result_pusher and result_sealer:
                result_sealer()
                reset_pusher()
            # finished.
        else:
            sync_flag_bagging = True
        #bagging ready
        return
    elif data.data == 911:
        sendToUser(0, error_code=3, error_msg="OUT OF BAGS")
        return
def sendToUser(flag, boot_message = "", progress_bar = 0, error_code = 0, error_msg = "",
                types=None, confidences = None):
    if not types:
        types = []
    if not confidences:
        confidences = []
    data = UserMsg()
    data.flag = flag
    data.boot_msg = boot_message
    data.progress_level = progress_bar
    data.error_code = error_code
    data.error_msg = error_msg
    data.types = types
    data.confidences = confidences
    user_publisher.publish(data)

def ctcCallback(data):
    global sync_flag_id
    global count_queue
    if not state_c:
        sendToUser(0, error_code=5, error_msg="UNEXPECTED STATE")
        return
    sendToLog(0, "Bread in position, let's go")
    if data.data == 2:
        rospy.loginfo("BREAD FOR ID: %d ", data.data)
    if count_queue>0:
        sync_flag_id = True
        slicer_publisher.publish(100)
        bag_publisher.publish(1000)
        count_queue-=1
        return
    else:
        
        identifier_publisher.publish(1)
        

def stcCallback(data):
    if data.data == 5:
        # Hand detected near blades

        sendToLog(2, "STOPPING EXECUTION")
        state[0] = False
        bag_publisher.publish(0)
        sendToUser(0, error_code=1, error_msg="REMOVE HAND FROM NEAR BLADES")
        conveyor_publisher.publish(0)
    elif data.data == 1:
        global sync_flag_id
        global sync_flag_slicer
        global sync_flag_bagging
        
        if sync_flag_id:
                if sync_flag_bagging:
                    sync_flag_bagging = False
                    sync_flag_slicer = False
                    sync_flag_bagging = False
                    #start pusher and fan
                    result_pusher = push_pusher()
                    result_sealer = push_sealer()
                    if result_pusher and result_sealer:
                        result_sealer()
                        reset_pusher()
                else:
                    sync_flag_slicer = True
        else:
                sync_flag_slicer = True
                
        return
    # DEMON ONLY:
    elif data.data == 1000:
        bag_publisher.publish(1000)

from bread_gazebo.srv import OverviewQueue, OverviewQueueResponse
def utcCallback(data):
    global sync_flag_id
    global sync_flag_slicer
    global sync_flag_bagging
    global count_queue
    if data.data == 1:
        if sync_flag_slicer:
            
            if sync_flag_bagging:
                sync_flag_bagging = False
                sync_flag_slicer = False
                sync_flag_bagging = False
                #start pusher and fan
                result_pusher = push_pusher()
                result_sealer = push_sealer()
                if result_pusher and result_sealer:
                    result_sealer()
                    reset_pusher()
            else:
                sync_flag_id = True
                bag_publisher.publish(1000)
        else:
            sync_flag_id = True
            if not sync_flag_bagging:
                bag_publisher.publish(1000)
        return
        # # User has put bread
        # sendToLog(0, "USER PUT BREAD IN, ADDING TO QUEUE")
        
        # sendToUser(2, types=["White", "Panini", "Black", "Brown"], confidences=[80, 10, 5, 2] )
        # # DEMO ONLY:
        # identifier_publisher.publish(1000)
    
    elif data.data == 5:
        # User window is closed/shutdown issued.
        rospy.signal_shutdown("User window closed")
    elif data.data == 0:
        # Start issued
        if state_c.on:
            return
        rospy.wait_for_service('Overview_Queue')
        try:
            overview_q = rospy.ServiceProxy('Overview_Queue', OverviewQueue)
            resp = overview_q(1)
            count_queue =len( resp.breads)
            
            
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
        state_c.on = True
        conveyor_publisher.publish(0)

def itcCallback(data):
    global count_queue
    if not state_c.on or state_c.em:
        sendToUser(0, error_code=5, error_msg="UNEXPECTED STATE")
        return
    
    sendToUser(2, types=data.name, confidences=data.score)
    slicer_publisher.publish(100)

def protective_caps_handler(pin):
    global state
    if GPIO.input(pin):
            sendToLog(1, "1")
            # RESUME ACTIVITY!
            
            print("ON\n")
            bag_publisher.publish(1)
            sendToLog(0, "PROTECTIVE CAPS ON")
            sendToUser(1)
            conveyor_publisher.publish(1)
    else:
            sendToLog(1, "0")
            # HERE NEED TO STOP FERRIS WHEEL AND SLICER
            
            print("Off\n")
            bag_publisher.publish(0)
            sendToLog(1, "ENSURE ALL PROTECTIVE CAPS ARE PROPERLY CLOSED")
            sendToUser(0, error_code=2, error_msg="PROTECTIVE CAPS OFF")
            conveyor_publisher.publish(0)


def push_pusher():
    rospy.loginfo("going to push pusher")
    goal = PusherGoal(required_status=1)
    pusher_client.send_goal_and_wait(goal)
    return pusher_client.get_result()

def push_sealer():
    goal = SealerGoal(required_status=1)
    sealer_client.send_goal_and_wait(goal)
    return sealer_client.get_result()

def reset_pusher():
    goal = PusherGoal(required_status=2)
    pusher_client.send_goal_and_wait(goal)
    return pusher_client.get_result()

def reset_sealer():
    goal = SealerGoal(required_status=2)
    sealer_client.send_goal_and_wait(goal)
    return sealer_client.get_result()

def publish_emergency():
    pass

def reset_emergency():
    pass

def emergency_callback(channel):
    input_signal = GPIO.input(emergency_in)
    if input_signal == GPIO.HIGH:
        publish_emergency()
    if input_signal == GPIO.LOW:
        reset_emergency()

def controllerInitialise():    
    rospy.init_node('controller', anonymous=False)
    rospy.on_shutdown(shutdown_routine)
    GPIO.add_event_detect(pin_caps, GPIO.BOTH, callback=protective_caps_handler)  
    rospy.Subscriber('bagging_to_controller', UInt32, btcCallback)
    rospy.Subscriber('conveyor_to_controller', UInt32, ctcCallback)
    rospy.Subscriber('slicer_to_controller', UInt32, stcCallback)
    rospy.Subscriber('user_to_controller', UInt32, utcCallback)
    rospy.Subscriber('identifier_to_controller',TfResult, itcCallback)
    rospy.loginfo("Started1111")
    rospy.loginfo("going to push pusher")
    # pusher_client.wait_for_server()
    # push_pusher()
    rospy.Rate(0.2).sleep()
    rospy.wait_for_service('User_Status')
    sendToUser(3, boot_message="Interface started", progress_bar=5)
    sendToLog(0, "USER UP")
    rospy.wait_for_service('Bagging_Status')
    sendToUser(3, boot_message="Bagging interface started", progress_bar=15)
    sendToLog(0, "BAGGING UP")
    try:
        rospy.wait_for_service('Slicer_Status', timeout = 15)
        sendToUser(3, boot_message="Slicer started", progress_bar=35)
        sendToLog(0, "SLICER UP")
    except rospy.ROSException as e:
        sendToUser(3, boot_message="Slicer failed to start slicer", progress_bar=35)
        sendToLog(1, "SLICER NOT RESPONDING")
    rospy.wait_for_service('Conveyor_Status')
    sendToUser(3, boot_message="Conveyor interface started", progress_bar=45)
    sendToLog(0, "CONVEYOR UP")
    rospy.wait_for_service('Loaf_Queue_Status')
    sendToUser(3, boot_message="Loaf Queue working", progress_bar=50)
    sendToLog(0, "LOAF Q UP")
    
    # pusher_client.wait_for_server()
    sendToUser(3, boot_message="Pusher working", progress_bar=60)
    sendToLog(0, "PUSHER UP")
    # sealer_client.wait_for_server()
    sendToUser(3, boot_message="Sealer working", progress_bar=70)
    sendToLog(0, "PUSHER UP")
    # time.sleep(2)
    sendToUser(1)
    slicer_publisher.publish(1)
    slicer_publisher.publish(100)
    # if not GPIO.input(pin_caps):
    #     state_c.em = True
    #     sendToLog(1, "off")
    #     bag_publisher.publish(0)
    #     sendToLog(1, "ENSURE ALL PROTECTIVE CAPS ARE PROPERLY CLOSED")
    #     sendToUser(0, error_code=2, error_msg="PROTECTIVE CAPS OFF")
    #     conveyor_publisher.publish(0)
    GPIO.add_event_detect(emergency_in,GPIO.BOTH,emergency_callback)
    rospy.spin()


if __name__ == '__main__':
    controllerInitialise()
