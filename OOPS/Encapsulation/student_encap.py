# 2. Design a Student class where marks:
# • should always be between 0 and 100
# • should never be set directly
# Enable updating marks only through a controlled method that performs range
# checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states
import sys


class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0
    def update_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")
    def get_marks(self):
        return self.__marks
s1=Student("Nikhil")
s1.update_marks(85)
print(s1.get_marks())
s1.update_marks(101) # here it doesn't work because it contains private encapsulation
print(s1.get_marks())