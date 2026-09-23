# 2. Build:
# • Vehicle base class
# • Car, Bike, Auto subclasses
# • A Driver class that contains a Vehicle
# • A Ride class that:
# o Calculates fare differently depending on the type of vehicle (polymorphism)
# o Stores driver + vehicle combination
# o Protects internal fare formula through encapsulation
# Also:
# • Use __str__ to print readable ride summaries.
# Show how composition + polymorphism interact.

class Vehicle:
    def fare(self,distance):
        pass
class Car(Vehicle):
    def fare(self,distance):
        return distance*10
class Bike(Vehicle):
    def fare(self,distance):
        return distance*5
class Auto(Vehicle):
    def fare(self,distance):
        return distance*7
class Driver:
    def __init__(self,name,vehicle):
        self.name=name
        self.vehicle=vehicle
class Ride:
    def __init__(self,driver,distance):
        self.driver=driver
        self.__fare=driver.vehicle.fare(distance)
    def __str__(self):
        return "Ride by " + self.driver.name + ", Fare: " + str(self.__fare)
d1=Driver("Nicky",Car())
r1=Ride(d1,10)
print(r1)