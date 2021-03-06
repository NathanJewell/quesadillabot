from DeviceTypes import *
from DeviceController import DeviceController
import time
import pdb
import math

if __name__ == "__main__":

    test_device_type = "UltrasonicSensor"

    
    controller = DeviceController("Controller")

    controller.load_config(f"test_configs/test_{test_device_type}.yaml")

    if test_device_type == "Motor":
        for x in range(100):
            rate = math.sin(x/6)
            controller.do("TEST", Motor.run_timed, (100, abs(rate), 1, False))
            time.sleep(.1)
        print("Running Motor")

        time.sleep(10)

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
