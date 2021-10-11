from DeviceTypes import *
from DeviceController import DeviceController
import time
import pdb
import math

if __name__ == "__main__":

    test_device_type = "UltrasonicSensor"

    
    controller = DeviceController("Controller")

    controller.load_config(f"handmovement.yaml")

    last_distance = 0
    def movement_callback(distance):
        distance_zero = 0
        distance_max = 20
        controller.do("MTR", Motor.run_timed, (100, 1, direction, False))
        time.sleep(.1)
        controller.do("TEST", Motor.stop, ())
    
    if test_device_type == "LimitSwitch":
        def limit_cb():
            print("-----------------")
            print("----TRIGGERED----")
            print("-----------------")

        value = controller.do("TEST", LimitSwitch.wait_trigger, (limit_cb,))
        time.sleep(10)

        print("WITH VALUE" + str(value))


    if test_device_type == "UltrasonicSensor":
        def distance_cb(distance):
            print(f"Distance is: \t{distance}")
        
        value = controller.do("TEST", UltrasonicSensor.trigger_recieve_timed, (distance_cb,))

        time.sleep(10)

        print("WITH VALUE" + str(value))