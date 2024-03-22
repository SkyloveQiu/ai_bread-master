import threading
from multiprocessing.dummy import Pool as ThreadPool

from festo.CMMO import CMMO

'''
    Gantry.py is the top level interface for controlling many CMMO's.
   
    This library is a simple API for controlling axes. 
'''

class Gantry:
    def __init__(self, CMMO_ip_addresses):
        """
        Initialize Gantry
        :param CMMO_ip_addresses: List of IP Address of the CMMO's
        """
        self.Moter = CMMO(CMMO_ip_addresses)

    def enable(self, verbose=False, veryVerbose=False):
        """
        Enable all of the motors for movement. Must call before moving or homing motors.
        :param verbose: print high level debugging information to the console
        :param veryVerbose: print low level debugging information to the console, useful for understanding CVE
        """
        s = self.Moter.enableControl(verbose=verbose, veryVerbose=veryVerbose)
        if s["ACK message"] != "Everything Ok":
            raise RuntimeError("Failed to Enable Control of Device at IP Address "
                                + self.Moter.ip_address + ": ERROR MESSAGE = " + str(s["ACK message"]))
        print("CMMO at", self.Moter.ip_address, "enabled")

        self.setPositionMode()

    def home(self, verbose=False, veryVerbose=False):
        """
        Home all motors.
        :param verbose: print high level debugging information to the console
        :param veryVerbose: print low level debugging information to the console, useful for understanding CVE
        """

        
        s = self.Moter.home(verbose=verbose, veryVerbose=veryVerbose)
        if s["ACK message"] != "Everything Ok":
            raise RuntimeError("Failed to Enable Control of Device at IP Address "
                                + self.Moter.ip_address + ": ERROR MESSAGE = " + str(s["ACK message"]))
        self.setPositionMode(verbose=verbose, veryVerbose=veryVerbose)

    def setPositionMode(self, verbose=False, veryVerbose=False):
        """
        Sets the motors into positioning mode in order to receive coordinates. Automatically called after enabling or homing.
        :param verbose: print high level debugging information to the console
        :param veryVerbose: print low level debugging information to the console, useful for understanding CVE
        """
        self.Moter.setPositioningMode(verbose=verbose, veryVerbose=veryVerbose)

    def resetError(self,verbose=False,veryVerbose=False):
        """
        Reset the error to disable mode. enable controll needs to be called.
        :param verbose: print high level debugging information to the console
        :param veryVerbose: print low level debugging information to the console, useful for understanding CVE
        """
        self.Moter.reset_error()

    def moveTo(self, record, velocities=None, verbose=False, veryVerbose=False):
        """
        Moves the motors to given coordinates.
        :param locations: list of locations corresponding to the given list of motors.
        :param velocities: list of desired motor velocities in mm/sec
        :param verbose: print high level debugging information to the console
        :param veryVerbose: print low level debugging information to the console, useful for understanding CVE
        """
        
        s = self.Moter.moveTo(record,verbose=False,veryVerbose=False)
        if s["ACK message"] != "Everything Ok":
                raise RuntimeError("Failed to Enable Control of Device at IP Address "
                                   + self.Moter.ip_address + ": ERROR MESSAGE = " + str(
                    s["ACK message"]))

    def disconnect(self):
        """
        disconnect from all CMMOs
        """
        self.Moter.finish()