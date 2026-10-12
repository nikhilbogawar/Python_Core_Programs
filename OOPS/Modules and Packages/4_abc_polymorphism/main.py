# 4. Create a package with a module containing an abstract base class (ABC).
# Another module in the same package should define concrete subclasses that
# implement all abstract methods. Write a driver program that imports these
# classes and demonstrates polymorphism.
from mypackage1.circle import Circle,Rectangle
for shape in [Circle(),Rectangle()]:
    print(shape.area())