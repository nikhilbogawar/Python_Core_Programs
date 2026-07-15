# create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# Demonstrate:
# 1.	Creating multiple students.
# 2.	Applying a grading curve.
# 3.	Displaying updated results with letter grades.

class Student:
    total_students = 0
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def is_passed(self):
        return self.marks >= Student.passing_marks

    @classmethod
    def curve_marks(cls, students, percent):
        for s in students:
            s.marks = s.marks + s.marks * (percent / 100)

    @staticmethod
    def grade(marks):
        if marks >= 75:
            return "A"
        elif marks >= 50:
            return "B"
        else:
            return "C"

s1 = Student("Nikhil", 75)
s2 = Student("Nicky", 35)
print(s1.name, s1.is_passed(), Student.grade(s1.marks))
print(s2.name, s2.is_passed(), Student.grade(s2.marks))

Student.curve_marks([s1, s2], 20)
print(s1.name, s1.is_passed(), Student.grade(s1.marks))
print(s2.name, s2.is_passed(), Student.grade(s2.marks))
