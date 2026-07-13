# Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

class Car:
    wheels=4
    def __init__(self, mileage):
        self.mileage=mileage

    def display_specs(self):
        print("Mileage:", self.mileage, "Wheels:", Car.wheels)

    @classmethod

    def change_wheels(cls, new_count):
        cls.wheels=new_count

c1=Car(18)
c1.display_specs()
Car.change_wheels(10)
c1.display_specs()