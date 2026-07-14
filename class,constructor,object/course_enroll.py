# Create a class Course that:
# •	Tracks total courses created.
# •	Each course has a title, duration, and enrolled_students.
# •	Provides a method to enroll a new student.
# •	Allows updating the minimum duration for a valid course across all instances.
# •	Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.	Creating multiple courses.
# 2.	Enrolling students.
# 3.	Updating minimum duration and checking durations.

class Course:
    total_courses = 0
    min_duration = 1

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = 0
        Course.total_courses += 1

    def enroll(self):
        self.enrolled_students += 1

    @classmethod
    def update_min_duration(cls, new_min):
        cls.min_duration = new_min

    @staticmethod
    def is_valid_duration(dur):
        return 0 < dur <= 60

c1 = Course("Python", 30)
c2 = Course("Java", 45)
c1.enroll()
c2.enroll()
print(c1.title, c1.enrolled_students)
print(c2.title, c2.enrolled_students)

Course.update_min_duration(10)
print(Course.is_valid_duration(70))