import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32, Int32
from bread_gazebo.msg import LogMsg,SpinWheelAction,SpinWheelGoal
import json
import os
import cv2 as cv
import time
import actionlib
import numpy as np
dirpath = os.path.dirname(os.path.realpath(__file__))
cam = cv.VideoCapture("/dev/video3")
x1 = 0
x2 = 0
y1 = 0
y2 = 0

wheel_client = actionlib.SimpleActionClient("spin_wheel",SpinWheelAction)
y_start = 20
y_end = 420
x_start = 200
x_end = 400
def sync_motor():
    global x1,x2,y1,y2
    
    time.sleep(5)
    if not cam.isOpened():
        raise IOError("Cannot open webcam")
    prev = None
    flag = True
    count = 0
    while not rospy.is_shutdown():
        
        # ret can be used to detect if capture was successful 
        ret, frame = cam.read()
        frame = frame[y_start:y_end, x_start: x_end]
        if count < 10:
            
            count+=1
            rospy.Rate(1).sleep()
            continue
        if not ret:
            continue
        
        frame_gr = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gr = cv.medianBlur(frame_gr, 11)
        if flag:
            lower = np.array([30, 80, 127], dtype = "uint8")
            upper = np.array([52, 100, 165], dtype = "uint8")
            # lower = np.array([39, 20, 35], dtype = "uint8")
            # upper = np.array([59, 50, 60], dtype = "uint8")
            mask = cv.inRange(frame, lower, upper)
            output = cv.bitwise_and(frame, frame, mask = mask)
            # ms  = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
            threshold = cv.threshold(mask, 20, 255, cv.THRESH_BINARY)[1]
            threshold = cv.dilate(threshold, None, iterations=1)
            
            cnts, _ = cv.findContours(threshold, cv.RETR_EXTERNAL,
            cv.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                if cv.contourArea(c) < 500 or cv.contourArea(c)>10000:
                    continue
                (x, y, w, h) = cv.boundingRect(c)
                print(str(x)+str(x+w))
                # (x1,y1,x2,y2) = (x,y,x+w,y+h)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.imwrite(dirpath+"/yellow.png", np.hstack([frame,output]))
            
            flag = False
            continue
        

        # MOVE FERRIS WHEEL 50 STEPS THEN :
        goal = SpinWheelGoal(angle_to_spin=50.0)
        wheel_client.send_goal_and_wait(goal)
        lower = np.array([30, 80, 127], dtype = "uint8")
        upper = np.array([52, 100, 165], dtype = "uint8")

        mask = cv.inRange(frame, lower, upper)
        output = cv.bitwise_and(frame, frame, mask = mask)
        # ms  = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        threshold = cv.threshold(mask, 20, 255, cv.THRESH_BINARY)[1]
        threshold = cv.dilate(threshold, None, iterations=1)
            
        cnts, _ = cv.findContours(threshold, cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv.contourArea(c) < 2000:
                continue
            (x, y, w, h) = cv.boundingRect(c)
            if x1-(x+w)<10:
                print("DONE")
                return
            
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv.imwrite(dirpath+"/blue.png", frame)
        

        
        rospy.Rate(8).sleep()
    