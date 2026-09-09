# Write a function total_area(shapes) that takes a list of any shape objects and
# returns their combined area. Use duck typing — any object with an area() method should work.
# Test with Circle, Rectangle, Triangle, and a custom class Hexagon.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Hexagon:
    def __init__(self, side):
        self.side = side
    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

def total_area(shapes):
    return sum(shape.area() for shape in shapes)

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7), Hexagon(2)]
print("Total Area:", total_area(shapes))
