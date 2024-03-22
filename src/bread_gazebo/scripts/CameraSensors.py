#!/usr/bin/env python3
from math import sqrt
import rospy
from bread_gazebo.msg import LogMsg
from std_msgs.msg import UInt32
from bread_gazebo.srv import BagCheckup,BagCheckupResponse
import cv2 as cv
import os
import time
from numpy import array_equiv
dirpath = os.path.dirname(os.path.realpath(__file__))
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
component_name = "Sensors Interface Bagging"
state = [False]
cam = cv.VideoCapture(0)

# TODO: THESE NEED TO BE IN CONFIG
treshold_difference = 120
x_start, x_end = 360, 480
y_start, y_end = 120, 330
default_values = [30, 31, 38]

def initialise_default() -> None:
    global default_values
    ret, img = cam.read()
    if not ret:
        raise IOError("Cannot take picture")
    background_image = cv.medianBlur(img[y_start:y_end, x_start: x_end],1)
    default_values = background_image.mean(axis=0).mean(axis=0)
    print(default_values)
    cv.imwrite("{dirpath}/background_bagging.png", background_image)
    print("\n!!!!!!! Took Background")
    return

def is_bag(default_values) -> bool:
    ret, img = cam.read()
    if not ret:
        raise IOError("Cannot take picture")
    
    img2 = cv.medianBlur(img[y_start:y_end, x_start: x_end],5)
    cv.imwrite("{dirpath}/bag_baggin.png", img2)
    average = img2.mean(axis=0).mean(axis=0)
    # rospy.loginfo('[%f, %f, %f]', average[0], average[1],average[2])
    difference = sqrt((average[0]-default_values[0])**2+(average[1]-default_values[1])**2+(average[2]-default_values[2])**2)
    # rospy.loginfo('DIFF NUMPY : %f', difference)
    return difference > treshold_difference

# open cv implementation for finding difference between two images. Should be quite fast
# used for: is there a bag of given type, is bread in position (though this last one i highly doubt will work)
def diff_two_images(img1, img2):
    img1_gr= cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    img2_gr = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    s = cv.norm(img1_gr, img2_gr, cv.NORM_L2)  
    return s

# opencv implementation of countouring. Could be used to detect if bread is in position in combination with a TF model
def contours(path_1, path_2):
    img1 = cv.imread(path_1)
    img1_gr= cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    img1_gr = cv.bilateralFilter(img1_gr, 20, 300, 300)
    img2 = cv.imread(path_2)
    
    img2_gr = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    img2_gr =  cv.bilateralFilter(img2_gr, 20, 300, 300)
    diff = cv.absdiff(img1_gr, img2_gr)
    threshold = cv.threshold(diff, 20, 255, cv.THRESH_BINARY)[1]
    threshold = cv.dilate(threshold, None, iterations=5)
    cv.imwrite("{dirpath}/threshold.png", threshold)
    cnts, _ = cv.findContours(threshold, cv.RETR_EXTERNAL,
		cv.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv.boundingRect(c)
        cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 0), 2)
    cv.imwrite(dirpath+"/contours.png", img2)

def webcam_demo():
    if not cam.isOpened():
        raise IOError("Cannot open webcam")
    prev = None
    flag = True
    while(True):
        # ret can be used to detect if capture was successful 
        ret, frame = cam.read()
        if not ret:
            continue
        # cv.imshow('frame', frame)

        # frame = cv.bilateralFilter(frame, 9, 100, 100)
        
        frame_gr= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gr = cv.medianBlur(frame_gr, 11)
        if flag:
            prev = frame_gr
            flag = False
        diff = cv.absdiff(prev, frame_gr)
        threshold = cv.threshold(diff, 20, 255, cv.THRESH_BINARY)[1]
        threshold = cv.dilate(threshold, None, iterations=5)
        
        cnts, _ = cv.findContours(threshold, cv.RETR_EXTERNAL,
            cv.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv.contourArea(c) < 4000:
                continue
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow('feed', frame)
        prev = frame_gr

        # Wait for esc in the video
        c = cv.waitKey(1)
        if c == 27:
            break
        # rospy.Rate(1).sleep()
    cleanup()
def bag_check_up_routine(req):
    try:
        if(array_equiv(default_values, [0,0,0])):
            initialise_default()
            return BagCheckupResponse(2)
        else:
            if is_bag(default_values):
                return BagCheckupResponse(1)
            else:
                return BagCheckupResponse(0)
    except IOError:
        return BagCheckupResponse(-1)


def sensorsInitialise():
    rospy.init_node('enough_bags', anonymous=False)
    # camera I used needed some time to start up
    time.sleep(3)

    if not cam.isOpened():
        raise IOError("Cannot open webcam")
    # s = diff_two_images (dirpath+'/background.jpg',dirpath+'/bag.jpg' )
    # contours(dirpath+'/background.jpg',dirpath+'/bag.jpg' )
    # print(s) 
    # webcam_demo()
    rospy.Service('Bag_Check', BagCheckup, bag_check_up_routine)
    rospy.spin()
    
def cleanup():
    cam.release()
    cv.destroyAllWindows()
if __name__ == '__main__':
    sensorsInitialise()