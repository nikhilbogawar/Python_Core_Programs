# 3. Student Result System
# Create a Student class with:
# • Name
# • marks
# • display_marks()
# Create a Result class that inherits Student and calculates whether the student has
# passed or failed.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_marks(self):
        print(f"Student Name : {self.name}")
        print(f"Marks : {self.marks}")
class Result(Student):
    def __init__(self,name,marks):
        super().__init__(name,marks)
    def check_result(self):
        if self.marks>=40:
            print("Result : Passed")
        else:
            print("Result : Failed")
# s1=Student("Nikhil",95)
# s1.display_marks()
r1=Result("Nikhil",95)
r1.display_marks()
r1.check_result()
r2=Result("Nicky",35)
r2.display_marks()
r2.check_result()