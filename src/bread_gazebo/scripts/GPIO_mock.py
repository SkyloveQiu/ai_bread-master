from time import sleep
import asyncio 
class GPIO(object):

    OUT = 1
    HIGH = 1
    LOW = 0
    BOARD = 0
    BOTH = 2
    IN = 0
    async def call(callback):
        # sleep(15)
        # callback(40)
        return 0
    def setmode(inp=0):
        return True
    def setup(arr, mode):
        return True
    def output(pin, out):
        return out
    def input(pin):
        return False
    def add_event_detect(pin_in, mode, callback=None):
        asyncio.run(GPIO.call(callback))
        return pin_in
    def cleanup():
        print("CLEANED")
        return 0
    