
from .Device import Device, DeviceException
import RPi.GPIO as GPIO
import time


class Motor(Device):
    def __init__(self):
        print("Motor Created")

    def initialize_config(self, config):
        try:
            self.initialize(
                config["name"],
                config["label"],
                config["pwm_gpio"],
                config["direction_a"],
                config["direction_b"]
            )
        except Exception as e:
            raise DeviceException("Error loading motor config." + str(e))
    
    def initialize(self, name, label, pwm, direction_a, direction_b):
        #config settings
        self.name = name
        self.label = label
        self.pwm_pin = pwm
        self.direction_pin_a = direction_a
        self.direction_pin_b = direction_b

        #unhooked settings
        self.speed_max = 1
        self.speed_min = 0
        self.speed_multiplier = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm_driver = GPIO.PWM(self.pwm_pin, 1000)
        self.pwm_driver.start(0) #start with duty cycle of 0

        GPIO.setup(self.direction_pin_a, GPIO.OUT)
        GPIO.setup(self.direction_pin_b, GPIO.OUT)

    def fraction_as_dutycycle(self, fraction):
        return max(min(fraction, self.speed_max), self.speed_min) * self.speed_multiplier * 100
    #designed to be run in a thread
    def run_timed(self, time_ms, speed_fraction=1, direction=1, stop=True):
        self.run(speed_fraction, direction)
        time.sleep(time_ms/1000)
        if stop:
            self.stop()

    def run(self, speed_fraction=1, direction=1):
        print("RUNNING MOTOR")
        GPIO.output(self.direction_pin_a, direction)
        GPIO.output(self.direction_pin_b, not direction)
        duty_cycle_percent = self.fraction_as_dutycycle(speed_fraction)
        print(duty_cycle_percent)
        self.pwm_driver.ChangeDutyCycle(duty_cycle_percent)

    def stop(self):
        GPIO.output(self.direction_pin_a, 0)
        GPIO.output(self.direction_pin_b, 0)
        self.pwm_driver.ChangeDutyCycle(0)
        print("STOPPING MOTOR")

    



