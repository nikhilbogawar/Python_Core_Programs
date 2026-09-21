# 13. Create:
# • Abstract class VehicleControl with methods accelerate(), brake(), steer()
# • Implement CarControl, BikeControl, TruckControl
# Demonstrate calling each through a single interface.

from abc import ABC, abstractmethod
class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def steer(self):
        pass
class CarControl(VehicleControl):
    def accelerate(self):
        print("car accelerated")
    def brake(self):
        print("car stopped")
    def steer(self):
        print("car steering")
class BikeControl(VehicleControl):
    def accelerate(self):
        print("bike accelerated")
    def brake(self):
        print("bike stopped")
    def steer(self):
        print("bike steering")
class TruckControl(VehicleControl):
    def accelerate(self):
        print("truck accelerated")
    def brake(self):
        print("truck stopped")
    def steer(self):
        print("truck steering")
vehicles=[CarControl(),BikeControl(),TruckControl()]
for i in vehicles:
    i.accelerate()
    i.brake()
    i.steer()