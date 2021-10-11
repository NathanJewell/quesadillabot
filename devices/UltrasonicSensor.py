from .Device import Device, DeviceException
import RPi.GPIO as GPIO
import time
import datetime

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
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.output(self.trigger_pin, 0)

    def trigger_recieve_timed(self, callback, timeout_ms=1000):
        start = datetime.datetime.now()
        current_limit_value = None
        while (datetime.datetime.now() - start).seconds/1000 < timeout_ms:
                distance = self.trigger_recieve()
                callback(distance)
        return 0



    def trigger_recieve(self):
        GPIO.output(self.trigger_pin, 1)
        time.sleep(.0001)
        GPIO.output(self.trigger_pin, 0)
        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()
        
        pulse_length= pulse_end - pulse_start
        distance = round(pulse_length * 17150, 2)
        return distance