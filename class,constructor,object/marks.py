# Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40

s1 = Student("Nikhil", 80)
s2 = Student("Nicky", 38)

print(s1.name, s1.is_passed())
print(s2.name, s2.is_passed())

