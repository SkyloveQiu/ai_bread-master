import Jetson.GPIO as GPIO
emergency_out = 40
GPIO.setmode(GPIO.BOARD)

GPIO.setup(emergency_out,GPIO.OUT)
GPIO.output(emergency_out, GPIO.HIGH)
while True:
    print("m")