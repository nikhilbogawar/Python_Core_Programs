# 6. Online Course Enrollment System Using Multilevel Inheritance
# Class 1: Course
# • Create a method fee(course) that returns the course fee.
# Class 2: Academy (inherits Course)
# Create the following methods:
# • courses() – Display available courses.
# • enroll() – Allow the user to enroll in multiple courses.
# • billing() – Display the total fee and add a registration fee of ₹100.
# Class 3: Student (inherits Academy)
# • Create an object and call the enroll() method.
class Course:
    def __init__(self):
        self.course_fees={"Python":3000,"Java":2500,"DS":5000,"Web-D":4000}
    def fee(self,course):
        return self.course_fees.get(course,0)

class Academy(Course):
    def __init__(self):
        super().__init__()
        self.enrolled_courses=[]
    def courses(self):
        print("Available Courses and Fees:")
        for course, fee in self.course_fees.items():
            print(f"{course}:{fee}rs")
    def enroll(self):
        while True:
            course=input("Enter course to enroll (or 'done' to finish): ")
            if course.lower()=="done":
                break
            if course in self.course_fees:
                self.enrolled_courses.append(course)
                print(f"Enrolled in {course}")
            else:
                print("Invalid course. Please try again")
    def billing(self):
        total_fee=sum(self.fee(course) for course in self.enrolled_courses)
        total_fee+=100
        print("\nBilling Details:")
        print("Course Enrolled:", ", ".join(self.enrolled_courses))
        print(f"Total Fee (including 100rs registration): {total_fee}")

class Student(Academy):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def start_enrollment(self):
        print(f"\nWelcome {self.name} to the Academy")
        self.courses()
        self.enroll()
        self.billing()
s1=Student("Nikhil")
s1.start_enrollment()