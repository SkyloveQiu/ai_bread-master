#!/usr/bin/env python3
import time
import math
import Jetson.GPIO as GPIO

# from GPIO_mock import GPIO # Simple mock for GPIOS
import rospy
from bread_gazebo.msg import LogMsg
from bread_gazebo.msg import SpinWheelAction, SpinWheelFeedback,SpinWheelResult
from std_msgs.msg import Float32, UInt32
from pid.PID import pid1, pid2
from threading import Thread
import actionlib
# topic command
# rostopic pub /ferris_wheel_control std_msgs/Float32 3
log_publisher = rospy.Publisher('log_topic', LogMsg, queue_size=10)
feedback_publisher = rospy.Publisher('fw_feedback', UInt32, queue_size=10)
component_name = "Ferris Wheel Interface"
feedback = SpinWheelFeedback()
result = SpinWheelResult()
enabled = True


enable_passive = True
def sendToLog(type, msg):
    data = LogMsg()
    data.type = type
    data.log_info = msg
    data.source = component_name
    log_publisher.publish(data)

def execute_cb(goal):
    steps_needed = goal.angle_to_spin
    for i in range (steps_needed):
            GPIO.output(step_pin, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(step_pin, GPIO.LOW)
            time.sleep(0.001)
    action_server.set_succeeded()
    # enable_passive = False
    # e_camera=goal.angle_to_spin
    # reach_goal()
    
    
action_server = actionlib.SimpleActionServer('spin_wheel', SpinWheelAction, execute_cb=execute_cb, auto_start = False)

# STATE
wrap_around_count = 0
flag_should_be_done = False
flag_has_started = False
ang_velocity = 0
e_camera = 0
motor_angle = 0                 # motor angle
angle_goal = 0
big_motor_angle = 0
#Pin assignments
step_pin = 32
dir_pin = 31
enable_pin = 24
flag_wrap = 0
#GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup([step_pin, dir_pin, enable_pin], GPIO.OUT)

duty_cycle = 0.5                     # Duty cycle of output signal

# Motor/setup related constants
step_angle = 1.8  # Angle per step in degrees
micro_stepping_factor = 1  # Amount of steps multiplication factor because of micro stepping
total_cycle_steps = (360/step_angle)*micro_stepping_factor
        


def fwm_control_callback(data):
    global e_camera
    print(data.data)
    e_camera = data.data


def velocity_control(ang_velocity):
    if abs(ang_velocity) < 0.01:
        return 0
    else:
        return abs((ang_velocity * total_cycle_steps)/(4*math.pi))


def reach_goal():
    sendToLog(2, "PREEMPT REQUESTED")
    action_server.set_aborted()

def set_goal(data):
    global flag_should_be_done
    global e_camera
    buffer_var = float('%.3f'%(data.data*math.pi*5/3))
    goal = 0
    big_motor_angle = wrap_around_count*2*math.pi + motor_angle
    if big_motor_angle > buffer_var:
        goal = buffer_var + 2*math.pi - big_motor_angle
    else:
        goal = buffer_var - big_motor_angle
    e_camera = goal*5
    flag_should_be_done = True

def ferris_wheel_motor_control_Initialise():
    global motor_angle
    global big_motor_angle
    global e_camera
    global flag_wrap
    global wrap_around_count
    estimated_motor_step_position = 0       # Initial position
    
    while not rospy.is_shutdown():
        if not enable_passive:
            continue
        copy_ang_vel = ang_velocity
        step_time_interval = velocity_control(copy_ang_vel)
        # print(str(copy_ang_vel)+" "+str(step_time_interval))

        if step_time_interval == 0:
            GPIO.output(step_pin, GPIO.LOW)  # Assign value 0V to pulse output
        if step_time_interval != 0:
            # sendToLog(0,"time int " + str(step_time_interval))
            # time.sleep(duty_cycle * step_time_interval)
            rospy.Rate((2 * step_time_interval)).sleep()
            if copy_ang_vel  < 0:               # THIS CAN CHANGE WHILE SLEEP!! IS THIS WANTED??
                GPIO.output(dir_pin, GPIO.LOW)  # Assign value 0V to direction output
                estimated_motor_step_position = estimated_motor_step_position - 1
                # sendToLog(0,"motor pos neg " + str(estimated_motor_step_position))
            else:
                GPIO.output(dir_pin, GPIO.HIGH)  # Assign value 3.3V to direction output
                estimated_motor_step_position = estimated_motor_step_position + 1
                # sendToLog(0,"motor pos " + str(estimated_motor_step_position))
            big_motor_angle += float('%.3f'%(0.002*math.pi))
            if big_motor_angle >= 2*math.pi:
                big_motor_angle = float('%.3f'%(big_motor_angle - 2*math.pi))
            elif big_motor_angle < 0:
                big_motor_angle = float('%.3f'%(big_motor_angle + 2*math.pi))
            if estimated_motor_step_position >= total_cycle_steps:
                wrap_around_count = (wrap_around_count +1)%5
                flag_wrap = 1
                if e_camera > 2*math.pi:
                    e_camera = e_camera - 2*math.pi
                sendToLog(0,"wrapped around 1 "+str(e_camera))
                estimated_motor_step_position = estimated_motor_step_position - total_cycle_steps
            elif estimated_motor_step_position < 0:
                wrap_around_count = (wrap_around_count - 1)%5
                if e_camera < 0:
                    e_camera = e_camera + 2*math.pi
                flag_wrap = -1
                sendToLog(0,"wrapped around -1 "+str(e_camera))
                estimated_motor_step_position = estimated_motor_step_position + total_cycle_steps
            else:
                flag_wrap = 0
            # Calculate angle from step position
            # TODO: MAKE SURE YOU DO NOT DELETE BY 0:
            motor_angle = 2 * math.pi * estimated_motor_step_position/total_cycle_steps
            # print(copy_ang_vel)
            GPIO.output(step_pin, GPIO.HIGH)  # Assign value 3.3V to pulse output
            # time.sleep(duty_cycle * step_time_interval) # BETTER TO USE ROSPY.RATE SLEEP
            rospy.Rate((2 * step_time_interval)).sleep()
            # limitting the rate on purpose for testing
            # rospy.Rate(20).sleep() 

            GPIO.output(step_pin, GPIO.LOW)  # Assign value 0V to pulse output
            

    GPIO.output(enable_pin, GPIO.HIGH)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)
    
counter = -1
def ferris_wheel_speed_control_Initialise():
        global counter 
        global ang_velocity
        global motor_angleflag_wrap
        global e_camera
        global flag_wrap
        global big_motor_angle
        global flag_should_be_done
        prev_e_camera = 0               # Previous displacement 
        prev_motor_angle = 0            # Previous motor angle
        pid1_error = 0                  # set point deviation used by pid1
        pid2_error = 0                  # set point deviation used by pid2
        prev_motor_speed = 0           # Previous motor speed
        dt = 0.00                       # One cycle time interval
        t1 = time.perf_counter()
        t2 = t1
        set_point_speed = 0             # set point speed
        motor_acceleration = 0          # motor acceleration
        pid1_error_estimation = True    # Enable or disable 
        mode = 'PID'                    # Control method used, either 'PID', 'acceleration' or 'speed'
        monitoring = True               # Enable or disable process monitoring
        
        
        while not rospy.is_shutdown():

            if not enabled:
                continue
            copy_angle = motor_angle
            copy_e_camera = e_camera
            
            if mode == 'PID':
                if pid1_error_estimation: 
                    
                    # estimation
                    if flag_wrap == 0:
                        d_angle = copy_angle - prev_motor_angle
                    elif flag_wrap == -1:
                        d_angle = prev_motor_angle + 2*math.pi - copy_angle
                        flag_wrap = 0
                        sendToLog(0, "flag -1 "+str(d_angle))
                    elif flag_wrap == 1:
                        d_angle =   copy_angle+ 2*math.pi - prev_motor_angle

                        sendToLog(0, "flag_+1 "+str(d_angle))
                        flag_wrap = 0
                    if d_angle > math.pi: # what if less than math.pi?
                        
                        sendToLog(0, "d_angle too large "+str(d_angle))
                        d_angle = d_angle - (2 * math.pi)
                        sendToLog(0, "L NOW IT IS "+str(d_angle))
                    if d_angle < -math.pi:
                        sendToLog(0, "d_angle too small "+str(d_angle))
                        d_angle = d_angle + (2 * math.pi)
                        sendToLog(0, "S NOW IT IS "+str(d_angle))
                    
                    if flag_should_be_done and ang_velocity < 0.001:
                        # sendToLog(0, "SMOL "+str(counter))
                        if counter < 3 and counter >= 0:
                            counter = counter+1
                        elif counter>=3:
                            print("done")
                            flag_should_be_done = False
                            counter = -1
                            feedback_publisher.publish(1)
                    else:
                        if flag_should_be_done and (ang_velocity > 0.01 or ang_velocity < -0.01):
                            counter = 0 
                        
                    if prev_e_camera != copy_e_camera:
                        
                        pid1_error = copy_e_camera - d_angle
                        # counter = 0
                        sendToLog(0, "New pid err "+str(pid1_error)+ " error camera is "+str(copy_e_camera) + " d_angle is "+str(d_angle))
                    else:
                        pid1_error = pid1_error - d_angle

                    # Update variables
                    prev_motor_angle = copy_angle
                    prev_e_camera = copy_e_camera

                else:
                    pid1_error = copy_e_camera
                    

                # Determine activeW integrator clamping
                    if copy_e_camera > pid1.int_clamp_margin:
                        pid1.integrator_clamping = True
                    else:
                        pid1.integrator_clamping = False

                # Compute dt and measure time
                t2 = time.perf_counter()  # Compute second measuring time
                dt = t2 - t1  # Compute time difference
                pid1.T = dt  # Change PID dt
                pid2.T = dt  # Change PID dt
                t1 = t2  # change variables

                # Compute pid1 control
                set_point_speed = pid1.PID_controller_update(pid1_error, copy_angle)

                # Compute pid2 
                pid2_error = set_point_speed - prev_motor_speed

                # Compute pid2 control
                motor_acceleration = pid2.PID_controller_update(pid2_error, prev_motor_speed)

            if mode == 'PID' or mode == 'acceleration':
                # Compute speed from acceleration
                motor_speed = prev_motor_speed + motor_acceleration * dt

                # Update variables
                prev_motor_speed = motor_speed

            if mode == 'PID' or mode == 'acceleration' or mode == 'speed':
                # Publish motor speed
                ang_velocity = motor_speed
        
def shutdown_routine():

    GPIO.cleanup()

# TODO: Check if one of the threads has died
def ferris_control_initialise():
    rospy.init_node('ferris_wheel_controller', anonymous=False)
    rospy.on_shutdown(shutdown_routine)
    rospy.Subscriber('ferris_wheel_control', Float32, fwm_control_callback)
    rospy.Subscriber('set_goal_wheel', UInt32, set_goal)
    motor_control = Thread(target=ferris_wheel_motor_control_Initialise)
    motor_control.setDaemon(True)
    motor_control.start()
    action_server.start()
    speed_control = Thread(target=ferris_wheel_speed_control_Initialise)
    speed_control.setDaemon(True)
    speed_control.start()
    motor_control.join()
    speed_control.join()
    # while not rospy.is_shutdown():
    
    #      GPIO.output(step_pin, GPIO.HIGH)
    #      time.sleep(0.01)
    #      GPIO.output(step_pin, GPIO.LOW)
    #      time.sleep(0.01)


if __name__ == '__main__':
    GPIO.output(enable_pin, GPIO.LOW)
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(step_pin, GPIO.LOW)
    ferris_control_initialise()
