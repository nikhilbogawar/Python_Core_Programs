# 11. Using abc module:
# • Create an abstract class Shape with area(), perimeter()
# • Implement Circle, Rectangle, Triangle
# Demonstrate:
# • why base class should NOT contain calculation logic
# • what happens if a subclass fails to implement one of the methods

from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 * math.pi * self.r
class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a + self.b + self.c)/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
sh=[Circle(5),Rectangle(4,5),Triangle(2,3,2)]
for i in sh:
    print(type(i).__name__, "Area:",i.area(), "Perimeter:",i.perimeter())

# If a subclass forgets to implement area() or perimeter(), Python raises TypeError when instantiating it.
# Base class should not contain calculation logic because each shape has different formulas.