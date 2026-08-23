# • Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding.
class Animal:
    def sound(self):
        print("Some generic animal sound")
class Dog:
    def sound(self):
        print("Bow Bow")
d1=Dog()
d1.sound()

# • Create class A with method show(). Create class B(A) that overrides show() and
# also calls the parent method using super().
class A:
    def show(self):
        print("Something A")
class B(A):
    def show(self):
        super().show()
        print("Something B")
s1=B()
s1.show()

# • Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.
class A:
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        print("Class B")
class C(B):
    def display(self):
        print("Class C")
c = C()
c.display()

# • Implement hierarchical inheritance using a base class Vehicle and two child
# classes Car and Bike, each defining a method wheels().
class Vehicle:
    def wheels(self):
        print("Vehicle has Wheels")
class Car(Vehicle):
    def wheels(self):
        print("Car contains 4 Wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike contains 2 Wheels")
car=Car()
bike=Bike()
car.wheels()
bike.wheels()

# • Create class Employee with an instance method salary(). Create class
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
# both outputs.
class Employee:
    def salary(self):
        return 30000
class Manager(Employee):
    def salary(self):
        base = super().salary()
        return base + 10000
e = Employee()
m = Manager()
print("Employee Salary:", e.salary())
print("Manager Salary:", m.salary())

# • Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class.
class University:
    uni_name = "ABC University"
    @classmethod
    def show_uni(cls):
        print("University:", cls.uni_name)
class College(University):
    pass
College.show_uni()

# • Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.
class MathOps:
    @staticmethod
    def add(a, b):
        return a + b
class AdvancedOps(MathOps):
    pass
print("Sum:", AdvancedOps.add(5, 7))

# • Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO.
class Father:
    def skills(self):
        print("Father: Gardening")
class Mother:
    def skills(self):
        print("Mother: Cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skills()

# • Create an abstract class Shape with an abstract method area(). Create class
# Rectangle(Shape) that implements the area() method.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
r = Rectangle(5, 3)
print("Rectangle Area:", r.area())

# • Create class Person with a constructor __init__(name). Create class
# Student(Person) with constructor __init__(name, roll). Use super() to call the
# parent constructor.
class Person:
    def __init__(self, name):
        self.name = name
        print("Person initialized:", name)
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        print("Student initialized:", name, "| Roll:", roll)
s = Student("Nikhil", 101)