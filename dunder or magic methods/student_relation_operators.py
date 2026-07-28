# True or False (Relational Operators in Dunder Methods)
class Student:
    def __init__(self,marks):
        self.marks=marks
    def __ge__(self,o2):
        return self.marks >= o2.marks
    def __gt__(self, o2):
        return self.marks > o2.marks
    def __eq__(self, o2):
        return self.marks==o2.marks
    def __ne__(self, o2):
        return self.marks!=o2.marks
s1=Student(85)
s2=Student(90)
print(s1>=s2)  # False
print(s1>s1)  # False
print(s1<=s2) # True
print(s1==s2)  # False
print(s1!=s2)  # True