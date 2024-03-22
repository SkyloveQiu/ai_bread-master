import Jetson.GPIO as GPIO
import time
enable_pin = 26
dir_pin = 29
step_pin = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup([enable_pin,dir_pin,step_pin],GPIO.OUT)
GPIO.output(enable_pin, GPIO.LOW)
GPIO.output(dir_pin, GPIO.HIGH)
GPIO.output(step_pin, GPIO.LOW)
for i in range (100):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(0.02)