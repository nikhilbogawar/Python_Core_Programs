# super() Chaining
# Write a class hierarchy School → Department → Course. Use super() in every
# __init__ to chain initialisation correctly. Each class adds one attribute. Prove that
# Manager(super()) in one class correctly delegates through the full chain.
class School:
    def __init__(self, name):
        self.name = name

class Department(School):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept

class Course(Department):
    def __init__(self, name, dept, course):
        super().__init__(name, dept)
        self.course = course

c = Course("ABC School", "Computer Science", "Python OOP")
print(c.name, c.dept, c.course)
