# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().
class Animal:
    def make_sound(self):
        print("Animal")
class Dog(Animal):
    def make_sound(self):
        print("Bow Bow")
class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
class Cow(Animal):
    def make_sound(self):
        print("Amba Amba")
l=[Dog(),Cat(),Cow()]
for i in l:
    i.make_sound()