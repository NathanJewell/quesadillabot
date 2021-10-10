
from devices.LimitSwitch import LimitSwitch
from devices.Motor import Motor
from devices.PowerRelay import PowerRelay
from devices.UltrasonicSensor import UltrasonicSensor
from devices.LED import LED



DeviceTypes = {
    "limit_switch" : LimitSwitch,
    "motor" : Motor,
    "power_relay" : PowerRelay,
    "ultrasonic_sensor" : UltrasonicSensor,
    "led" : LED
}