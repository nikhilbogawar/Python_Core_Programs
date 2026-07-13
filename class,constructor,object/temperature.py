# create a class Temperature with:
# •	instance attribute Celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def show_conversion(self):
        print("Celsius:", self.celsius, "Fahrenheit:", Temperature.to_fahrenheit(self.celsius))

t = Temperature(25)
t.show_conversion()
