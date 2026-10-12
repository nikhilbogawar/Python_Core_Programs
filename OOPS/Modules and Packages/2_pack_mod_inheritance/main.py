# 2. Create a Python package that contains two or more modules. Each module should
# define classes with attributes and methods. Then create another module outside
# the package, import the package modules, and create a subclass that inherits
# from at least one of the classes. Finally, create objects of both parent and
# child classes.
from mypackage.student import Student
from mypackage.teacher import Teacher

class Monitor(Student):
    def duty(self):
        print("Class Monitor")
s=Student()
t=Teacher()
m=Monitor()

s.display()
t.teach()
m.display()
m.duty()