# 5. Classes:
# • User
# • Instructor(User)
# • Student(User)
# • TeachingAssistant(Student, Instructor)
# Requirements:
# • Track course assignments privately
# • Ensure TAs override submit_work() and grade_work()
# • Print MRO and explain how Python resolves conflicts
class User:
    pass
class Instructor(User):
    pass
class Student(User):
    pass
class TeachingAssistant(Student, Instructor):
    def submit_work(self):
        return "TA submits work"
    def grade_work(self):
        return "TA grades work"
print(TeachingAssistant.mro())
