# • Create a base class Shape with a method area() that raises NotImplementedError.
# Create a child class Rectangle that overrides and implements the area method.
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
r = Rectangle(10, 5)
print("Area:", r.area())