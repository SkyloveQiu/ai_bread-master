#!/usr/bin/env python3
from asyncio.tasks import current_task
from PyQt5 import QtCore, QtWidgets
import rospy
from bread_gazebo.msg import LogMsg, UserMsg
import os
import time
import asyncio
from ui_scripts import *
import threading
from std_msgs.msg import UInt32
from bread_gazebo.srv import EnqueueLoaf, EnqueueLoafResponse
from bread_gazebo.srv import OverviewQueue, OverviewQueueResponse
from bread_gazebo.srv import UserStatus, UserStatusResponse
# TODO: CLEAN UP THE CODE... A LOT.
# TODO: FIX MAGIC VALUES
dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
controller_publisher = rospy.Publisher('user_to_controller', UInt32, queue_size=10)
component_name = "USER INTERFACE"
app = QtWidgets.QApplication([])
MainWindow = QtWidgets.QMainWindow()
loop = asyncio.new_event_loop()

loop_thread = None
def shutdown_routine():
    sendToLog(0, "SHUTTING")
    MainWindow.destroy()
    app.closeAllWindows()
    app.exit(0)
    app.quit()
    cleanup()
    return 0


def switch_to_add_loaf(input):
    ui = state.loaf_input_view
    ui.setupUi(MainWindow)
    MainWindow.show()
def close_down():
    print("CLOSING")
    rospy.signal_shutdown("SYNCHRONOUS CLOSE ISSUED")

def switch_to_overview(input):
    rospy.wait_for_service('Overview_Queue')
    try:
        overview_q = rospy.ServiceProxy('Overview_Queue', OverviewQueue)
        resp = overview_q(1)
        state.queue_overview_page.info= resp.breads
        ui = state.queue_overview_page
        
        ui.setupUi(MainWindow)
        MainWindow.show()
        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
def sendToLog(type, msg):
    data = LogMsg()
    data.type = type 
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)
def change_to_info(input):
    ui = state.info_page_view
    ui.setupUi(MainWindow)
    MainWindow.show()   
def switch_to_shtdwn_conf(input):
    ui = state.confirmation_shutdown
    ui.setupUi(MainWindow)
    MainWindow.show() 

def switch_to_start_conf(input):
    ui = state.confirmation_start
    ui.setupUi(MainWindow)
    MainWindow.show() 

def shutdown_callbak(x):

    app.closeAllWindows()
    app.exit(0)
    app.quit()
def confirm_callback(x):
    if len(state.loaf_input_view.loaf_count) != len(state.loaf_input_view.loaves):
        raise Exception()
    for x, bread_type in enumerate(state.loaf_input_view.loaves):
        for i in range(state.loaf_input_view.loaf_count[x]):
            try:
                enqueue_loaf = rospy.ServiceProxy('Loaf_Queue_Enqueue', EnqueueLoaf)
                resp = enqueue_loaf(1, bread_type)
    
            except rospy.ServiceException as e:
                print("Service call failed: %s"%e)
    state.loaf_input_view.loaf_count = []
    state.loaf_input_view.loaves = []
    state.main_menu_signal.emit(0)
def cancel_callback(x):
    state.main_menu_signal.emit(0)
def start_callback(x):
    controller_publisher.publish(0)
    state.main_menu_signal.emit(0)
def switch_to_main_menu(input):
    ui = state.main_menu_view
    ui.setupUi(MainWindow)
    MainWindow.show()
class State_Keepeer(QtCore.QObject):
    error_signal = QtCore.pyqtSignal(Error_Message)
    boot_info = QtCore.pyqtSignal(Boot_Message)
    bread_select_signal = QtCore.pyqtSignal(int)
    bread_select_view = Bread_Select()
    error_view = Error_View("", "")
    ui_start_up = Ui_Start_Up()
    main_menu_view = Main_Window(switch_to_queue=switch_to_overview, switch_to_info=change_to_info, start=switch_to_start_conf, shutdown=switch_to_shtdwn_conf,
    add_bread= switch_to_add_loaf)
    main_menu_signal = QtCore.pyqtSignal(int)
    info_page_view = Info_Window()
    info_page_signal = QtCore.pyqtSignal(int)
    queue_overview_signal = QtCore.pyqtSignal(int)
    queue_overview_page = Queue_Overview(switch_to_main_menu)
    confirmation_shutdown = Shutdown_confirmation(shutdown_callbak, cancel_callback)
    confirmation_start = Start_Confirmation(start_callback, cancel_callback)
    loaf_input_view = Loaf_Input(confirm_callback, cancel_callback)
    loaf_signal = QtCore.pyqtSignal(int)
    start_signal = QtCore.pyqtSignal(int)
    shtdwn_signal = QtCore.pyqtSignal(int)
    position = 0
    curr_task = 0

state = State_Keepeer()


bag_publisher = rospy.Publisher('controller_to_bagging', UInt32, queue_size=10)
def enqueue_loaf(bread_type, timeout_task: asyncio.Task = None, task_id: int = 0):
    if timeout_task:
        timeout_task.cancel()
    try:
        enqueue_loaf = rospy.ServiceProxy('Loaf_Queue_Enqueue', EnqueueLoaf)
        resp = enqueue_loaf(1, bread_type)
        
        controller_publisher.publish(1)
        if task_id == state.curr_task:
            state.main_menu_signal.emit(0)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def callback_generator(bread_type, timeout_func, task_id):
    return lambda e: enqueue_loaf(bread_type, timeout_func, task_id)


async def timeout_function(top_bread, task_id: int):
    sendToLog(1, "TIMEOUT!! start ss" )
    await asyncio.sleep(7)
    print("TIMEOUT!!!!!!")
    enqueue_loaf(top_bread, task_id=task_id)
    return
    

def ctu_callback(data):
    if data.flag == 0:
        turn_leds(data.error_code+8)
        start_buzzer()

        err = Error_Message()
        err.error_code=data.error_code
        err.error_message = data.error_msg
        state.error_signal.emit(err)
        state.position = 5
        # TODO: Change this to callback of some sort
        time.sleep(1)
        print("Stopping buzzer")
        stop_buzzer()
    elif data.flag == 1:
        turn_leds(16)
        state.position = 0
        sendToLog(0, "STARTING")
        state.main_menu_signal.emit(0)
    elif data.flag == 2:
        turn_leds(16 + 1)
        sendToLog(0, "CHOOSING BREAD")
        asyncio.set_event_loop(loop)
        state.curr_task = (state.curr_task+1)%100
        task = asyncio.run_coroutine_threadsafe(timeout_function(data.types[0], state.curr_task), loop)
        state.bread_select_view.callback_arr=[callback_generator(x,task, state.curr_task) for x in data.types]
        state.bread_select_view.confidence=data.confidences
        state.bread_select_view.info=data.types
        state.position = 3
        state.bread_select_signal.emit(0)

    elif data.flag == 3:
        if state.position != 0:
            return
        turn_leds(16)
        msg = Boot_Message()
        msg.boot_message = data.boot_msg
        msg.progress_level = data.progress_level
        state.boot_info.emit(msg)
    elif data.flag == 5:
        rospy.signal_shutdown("Async Shutdown")

def switch_to_error(err: Error_Message):
    sendToLog(0, "SWITCHING TO ERROR")
    ui = state.error_view
    ui.error_msg = err.error_message
    ui.error_code = err.error_code
    ui.setupUi(MainWindow)
    MainWindow.show()

def switch_to_bread_select(input):
    ui = state.bread_select_view
    ui.setupUi(MainWindow)
    MainWindow.show()



def add_info_to_startup(msg: Boot_Message):
    state.ui_start_up.change_progress(msg.progress_level)
    state.ui_start_up.append_output(msg.boot_message)


    
def status_ping(req):
    if req.flag == 5:
        sendToLog(0, "User going down")
        loop_thread = threading.Thread(target=close_down)
        loop_thread.setDaemon(True)
        loop_thread.start()
        return UserStatusResponse(0, "CLOSING")
def uiInitialise(): 
    global loop_thread   
    rospy.init_node('user_interface', anonymous=False)
    rospy.on_shutdown(shutdown_routine)
    rospy.Subscriber('controller_to_user', UserMsg, ctu_callback)
    rospy.Service('User_Status', UserStatus, status_ping)
    ui = state.ui_start_up
    ui.setupUi(MainWindow)
    state.queue_overview_signal.connect(switch_to_overview)
    state.error_signal.connect(switch_to_error)
    state.boot_info.connect(add_info_to_startup)
    state.main_menu_signal.connect(switch_to_main_menu)
    state.bread_select_signal.connect(switch_to_bread_select)
    state.start_signal.connect(switch_to_start_conf)
    state.shtdwn_signal.connect(switch_to_shtdwn_conf)
    state.loaf_signal.connect(switch_to_add_loaf)
    # Event loop needs to be on a separate thread :/
    loop_thread = threading.Thread(target=loop.run_forever)
    loop_thread.setDaemon(True)
    loop_thread.start()
    
    MainWindow.show()
    app.exec()
    sendToLog(0, "WINDOW CLOSED")
    # If we get here -> window has been closed
    controller_publisher.publish(5)
    rospy.signal_shutdown("WINDOW CLOSED")
    
    

if __name__ == '__main__':
    uiInitialise()


    
    
