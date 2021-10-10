
from devices.LimitSwitch import LimitSwitch
from devices.Motor import Motor
from devices.PowerRelay import PowerRelay
from devices.UltrasonicSensor import UltrasonicSensor
from devices.LED import LED



DeviceTypes = {
    "LimitSwitch" : LimitSwitch,
    "Motor" : Motor,
    "PowerRelay" : PowerRelay,
    "UltrasonicSensor" : UltrasonicSensor,
    "LED" : LED
}