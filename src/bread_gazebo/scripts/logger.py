#!/usr/bin/env python3
import rospy
from bread_gazebo.msg import LogMsg
import time
from datetime import datetime
import os
import csv

row = ['Nikhil', 'COE', '2', '9.0']
header=["Timestamp", "Source", "Message Type", "Data" ]
dirpath = os.path.dirname(os.path.realpath(__file__))
message_types_dictionary = {
    0: "INFO",
    1: "ERROR",
    2: "WARNING"
}


def addToLog(data):
    name_of_file = datetime.now().strftime("%d_%m_%Y")
    
    # with open(dirpath+"/"+name_of_file, "a+") as myfile:
    #     message_type = message_types_dictionary[data.type]
    #     source = data.source
    #     myfile.write('[{timestamp}]: {typemsg} [{datafrom}] {datamsg}\n'
    #     .format(timestamp = time.time(), typemsg = message_type, datamsg = data.log_info, datafrom = source))

    #     myfile.close()


    if not os.path.exists(dirpath+"/logs/"+name_of_file+".csv"):
        with open (dirpath+"/logs/"+name_of_file+".csv",'a+') as filecsv:
            csv.writer(filecsv).writerow(header)

    with open (dirpath+"/logs/"+name_of_file+".csv",'a+') as filecsv:                            
        writer = csv.DictWriter(filecsv, delimiter=',', fieldnames=header)
        f = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')
        writer.writerow({"Timestamp":f , "Source": data.source, "Message Type": message_types_dictionary[data.type], "Data": data.log_info}) 
        

        
# Topic callback function.
def callbackFunction(data):
    if data.type == 5:
        rospy.signal_shutdown("ASYNC CLOSE ISSUED")
        return 
    rospy.loginfo('[%d] %s MSG TYPE: %d from [%s]', time.time(), data.log_info, data.type, data.source)
    addToLog(data)

def logInitialise():

   
    rospy.init_node('logger_node', anonymous=False)
    rospy.Subscriber('log_topic', LogMsg, callbackFunction)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    logInitialise()
