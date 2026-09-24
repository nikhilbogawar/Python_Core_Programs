# 13.
# Build:
# • Transport abstract class
# • Subclasses: Taxi, Bus, Train
# • Each implements:
# o calculate_fare() differently
# • Use static method to validate distance
# • Encapsulate fare state
# • Add class method to update government tax slab
from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self, base_fare):
        self.__fare = base_fare
    @abstractmethod
    def calculate_fare(self, distance):
        pass
    @staticmethod
    def validate_distance(distance):
        if distance > 0:
            return True
        else:
            return False
    @classmethod
    def update_tax(cls, tax_rate):
        cls.tax_rate = tax_rate
class Taxi(Transport):
    def calculate_fare(self, distance):
        if self.validate_distance(distance):
            return distance * 15
class Bus(Transport):
    def calculate_fare(self, distance):
        if self.validate_distance(distance):
            return distance * 5
class Train(Transport):
    def calculate_fare(self, distance):
        if self.validate_distance(distance):
            return distance * 8
vehicles = [Taxi(0), Bus(0), Train(0)]
for v in vehicles:
    print(type(v).__name__, v.calculate_fare(10))