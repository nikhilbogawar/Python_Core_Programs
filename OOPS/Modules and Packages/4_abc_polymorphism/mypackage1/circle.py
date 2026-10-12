from mypackage1.shapes import Shape
class Circle(Shape):
    def area(self):
        return 3.14*5*5
class Rectangle(Shape):
    def area(self):
        return 4*6