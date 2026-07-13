# Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result

class Student:
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")

    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks

    @staticmethod
    def grade_category(marks):
        if marks >= 75:
            return "A"
        elif marks >= 50:
            return "B"
        else:
            return "C"
print("Marks List:")
s1 = Student("Nikhil", 85)
s2 = Student("Nicky", 35)

s1.result()
s2.result()

Student.update_passing_marks(30)
print("Updated Marks List:")
s1.result()
s2.result()

print(s1.name, "Grade:", Student.grade_category(s1.marks))
print(s2.name, "Grade:", Student.grade_category(s2.marks))
