
from .Device import Device, DeviceException
import RPi.GPIO as GPIO

class PowerRelay(Device):
    def __init__(self):
        pass

    def initialize_config(self, config):
        try:
            self.initialize(
                config["name"],
                config["label"],
                config["physical_pin"],
                config["type"]
            )
        except Exception as e:
            raise DeviceException("Could not load relay config." + e.message)


    def initialize(self, name, label, pin, NONC="NO"):
        self.name = name
        self.label = label
        self.pin = pin

        #NO is True, NC is False
        #defaults to NC in this logic even if string is otherwise
        self.type = True if NONC == "NO" else False
        GPIO.setup(self.pin, GPIO.OUT)

    def open(self):
        GPIO.output(self.pin, not self.type)

    def close(self):
        GPIO.output(self.pin, self.type)