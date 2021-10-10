from .Device import Device, DeviceException
import RPi.GPIO as GPIO

class UltrasonicSensor(Device):
    def __init__(self):
        pass

    def initialize_config(self, config):
        try:
            self.initialize(
                config["name"],
                config["label"],
                config["trigger_pin"],
                config["echo_pin"]
            )
        except Exception as e:
            raise DeviceException("Could not load Ultrasonic Sensor configuration." + e.message)
    
    def initialize(self, name, label, trigger, echo):
        self.name = name
        self.label = label
        self.trigger_pin = trigger
        self.echo_pin = echo

        GPIO.setmode(GPIO.BCM)