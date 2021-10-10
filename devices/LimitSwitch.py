from .Device import Device, DeviceException
import datetime
import RPi.GPIO as GPIO

class LimitSwitch(Device):
    def __init__(self):
        pass

    def initialize_config(self, config):
        try:
            self.intialize(
                config["name"],
                config["label"],
                config["physical_pin"]
                )
        except Exception as e:
            raise DeviceException(e.message)


    def initialize(self, name, label, pin):
        self.name = name
        self.label = label
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #get the limit switch value
        self.limit_value = lambda: GPIO.input(self.pin)


    #designed to be threaded if desired, 
    #executes the callback function synchronously 
    # and returns the limit value whenever a limit is triggered
    #timeout given in ms
    #returns -1 on timeout
    def limit_listener(self, callback, timeout=10000, starting_limit_value=None):
        start = datetime.datetime.now()
        if starting_limit_value == None:
            starting_limit_value = self.limit_value()
        current_limit_value = None
        while start - datetime.datetime.now().milliseconds < timeout:
            current_limit_value = self.limit_value()
            if current_limit_value != starting_limit_value:
                callback()
                return current_limit_value
        return -1





        