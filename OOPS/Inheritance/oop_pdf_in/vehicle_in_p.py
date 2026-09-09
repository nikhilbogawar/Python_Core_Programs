# Create a child class Car(Vehicle) that adds a doors attribute and overrides info() to
# include doors. Create ElectricCar(Car) that adds battery_range a
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def info(self):
        return super().info() + f", {self.doors} doors"


class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_range):
        super().__init__(make, model, year, doors)
        self.battery_range = battery_range

    def info(self):
        return super().info() + f", Range: {self.battery_range} km"


ecar = ElectricCar("Tesla", "Model 3", 2024, 4, 500)
print(ecar.info())
