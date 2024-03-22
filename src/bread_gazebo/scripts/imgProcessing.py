#!/usr/bin/env python3
import rospy
import numpy as np
from skimage import io
import os
from json import load
from math import sqrt

dirpath = os.path.dirname(os.path.realpath(__file__))

def avgColour(default_valuesz):
    default = io.imread(dirpath+"/background_bagging.png")[:, :, :]
    img = io.imread(dirpath+"/bag_baggin.png")[:, :, :]
    average = img.mean(axis=0).mean(axis=0)
    default_values = default.mean(axis=0).mean(axis=0)
    rospy.loginfo('[%f, %f, %f]', average[0], average[1],average[2])
    difference = sqrt((average[0]-default_values[0])**2+(average[1]-default_values[1])**2+(average[2]-default_values[2])**2)
    rospy.loginfo('DIFF : %f', difference)

def initialiseNode():

    with open(dirpath+'/config/config.json') as f:
        data = load(f)
    rospy.init_node('imgProcessing', anonymous=False)
    avgColour([data["default_red"], data["default_green"], data["default_blue"]])

if __name__ == '__main__':
    # initialiseNode()
    print("LEGACY - HAS BEEN REMOVED")

