from DeviceTypes import *
from DeviceController import DeviceController
import time
import pdb
import math

if __name__ == "__main__":

    test_device_type = "Motor"
    controller = DeviceController("Controller")

    controller.load_config(f"test_configs/test_{test_device_type}.yaml")

    for x in range(100):
        rate = math.sin(x/6)
        controller.do("TEST", Motor.run_timed, (100, abs(rate), 1, False))
        controller.do("TEST2", Motor.run_timed, (100, abs(rate), 1, False))
        time.sleep(.1)
    print("Running Motor")


    time.sleep(10)

    controller.do("TEST", Motor.stop, ())
    controller.do("TEST2", Motor.stop, ())