# • Create a class Student with an attribute marks.
# Implement a method set_marks(marks) that raises a ValueError if marks are not in the range 0 to 100
class Student:
    def __init__(self):
        self.marks = 0
    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.marks = marks
s = Student()
try:
    s.set_marks(120)
except ValueError as e:
    print("Error:", e)