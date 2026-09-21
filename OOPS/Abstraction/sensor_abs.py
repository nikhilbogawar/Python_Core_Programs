# 20. Design:
# • Abstract base class Sensor with functions read_value() and calibrate()
# • Subclasses: TemperatureSensor, PressureSensor, HumiditySensor
# Encapsulate:
# • internal raw sensor readings
# • calibration factor
# Hide all raw operations and allow only a public, clean get_reading() method.

from abc import ABC, abstractmethod
class Sensor(ABC):
    def __init__(self, raw_value, calibration_factor):
        self._raw_value = raw_value
        self._calibration_factor = calibration_factor
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
    def get_reading(self):
        return self.read_value() * self._calibration_factor
class TemperatureSensor(Sensor):
    def read_value(self):
        return self._raw_value
    def calibrate(self):
        print("Temperature sensor calibrated")
class PressureSensor(Sensor):
    def read_value(self):
        return self._raw_value
    def calibrate(self):
        print("Pressure sensor calibrated")
class HumiditySensor(Sensor):
    def read_value(self):
        return self._raw_value
    def calibrate(self):
        print("Humidity sensor calibrated")
sensors = [
    TemperatureSensor(30, 1.1),
    PressureSensor(100, 0.95),
    HumiditySensor(60, 1.05)
]
for s in sensors:
    s.calibrate()
    print(type(s).__name__, "Reading:", s.get_reading())
