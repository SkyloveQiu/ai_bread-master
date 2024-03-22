from GPIO_mock import GPIO
sound_out = 7  # sound VD
LED_Green = 11 
LED_Red =  12
LED_0 =  13
LED_1 =  16
LED_2 =  18
# LED_3 =  36
# LED_4 = 29
GPIO.setmode(GPIO.BOARD)
LED_array = [LED_Green, LED_Red, LED_0, LED_1, LED_2]
arr_out = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
GPIO.setup((LED_Green, LED_Red, LED_0, LED_1, LED_2), GPIO.OUT)
GPIO.setup(sound_out, GPIO.OUT)


def turn_leds(values):
    i = 0
    while i < len(LED_array):
        if values%2 == 1:
            arr_out[len(LED_array) - 1 -i]= GPIO.HIGH
        else:
            arr_out[len(LED_array) - 1 -i] = GPIO.LOW
        values = int(values/2)
        print(values)
        i += 1
    print(arr_out)
    GPIO.output(LED_array, arr_out)

def stop_buzzer():
    print("Stopping buzzer")
    GPIO.output(sound_out, GPIO.LOW)

def start_buzzer():
    GPIO.output(sound_out, GPIO.HIGH)
def all_set(value):
    if value:
        GPIO.output(LED_array, GPIO.HIGH)
    else:
        GPIO.output(LED_array, GPIO.LOW)

def cleanup():
    GPIO.cleanup()