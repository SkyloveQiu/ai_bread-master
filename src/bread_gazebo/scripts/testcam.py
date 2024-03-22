#!/usr/bin/env python3
from math import sqrt
import rospy
import cv2 as cv
import os
import time

dirpath = os.path.dirname(os.path.realpath(__file__))
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=640,
    display_height=360,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor_id=0 ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
cam = cv.VideoCapture(3)
# cam = cv.VideoCapture(2)
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
enable_pin = 26
dir_pin = 29
step_pin = 33

GPIO.setup([enable_pin,dir_pin,step_pin], GPIO.OUT)
# GPIO.setup(pin_caps, GPIO.IN)

GPIO.output(enable_pin, GPIO.LOW)
print("init with high")
GPIO.output(dir_pin, GPIO.HIGH)
GPIO.output(step_pin, GPIO.LOW)
y_start = 100
y_end = 300
x_start = 360
x_end = 480
if __name__ == '__main__':
    while True:
        ret, img = cam.read()
    # if not ret:
    #     raise IOError("Cannot take picture")
    
    # img2 = cv.medianBlur(img[y_start:y_end, x_start: x_end],5)
   
    # average = img2.mean(axis=0).mean(axis=0)
    # print(average)
    # for i in range(100):
    
    #      GPIO.output(step_pin, GPIO.HIGH)
    #      time.sleep(0.01)
    #      GPIO.output(step_pin, GPIO.LOW)
    #      time.sleep(0.01)
    # time.sleep(10)
    # GPIO.output(dir_pin, GPIO.LOW)
    # for i in range(100):
    
    #      GPIO.output(step_pin, GPIO.HIGH)
    #      time.sleep(0.01)
    #      GPIO.output(step_pin, GPIO.LOW)
    #      time.sleep(0.01)
    # GPIO.cleanup()
        cv.imwrite(dirpath+"/img113.png", img)
    
    
    
