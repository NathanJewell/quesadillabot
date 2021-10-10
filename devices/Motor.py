
from Device import Device, DeviceException
import RPi.GPIO as GPIO
import time


def Motor(Device):
    def __init__(self):
        pass

    def initialize_config(self, config):
        try:
            self.initialize(
                config["name"],
                config["label"],
                config["pwm_gpio"],
                config["direction_gpio"],
            )
        except Exception as e:
            raise DeviceException("Error loading motor config." + e.message)
    
    def initialize(self, name, label, pwm, direction):
        #config settings
        self.name = name
        self.label = label
        self.pwm_pin = pwm
        self.direction_pin = direction

        #unhooked settings
        self.speed_max = 1
        self.speed_min = 0
        self.speed_multiplier = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm_driver = GPIO.PWM(self.pwm_pin, 1000)
        self.pwm_driver.start(0) #start with duty cycle of 0

    def fraction_as_dutycycle(self, fraction):
        return max(min(fraction, self.speed_max), self.speed_min) * self.speed_multiplier
    #designed to be run in a thread
    def run_timed(self, time_ms, speed_fraction=1, direction=1):
        self.run(speed_fraction, direction)
        time.sleep(time_ms)
        self.stop()

    def run(self, time_ms, speed_fraction=1, direction=1):
        self.pwm_driver.ChangeDutyCycle(self.fraction_as_dutycycle(speed_fraction))

    def stop(self):
        self.pwm_driver.ChangeDutyCycle(0)

    



