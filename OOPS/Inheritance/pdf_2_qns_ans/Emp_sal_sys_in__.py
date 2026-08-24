# 2. Employee Salary System
# Create an Employee class with:
# • emp_name
# • salary
# • display_details()
# Create a Manager class that inherits Employee and adds a bonus(). Display the
# total salary.
class Employee:
    def __init__(self,emp_name,salary):
        self.salary=salary
        self.emp_name=emp_name
    def display_details(self):
        print(f"Employee Name : {self.emp_name}")
        print(f"Employee Salary : {self.salary}")
class Manager(Employee):
    def __init__(self,emp_name,salary,bonus):
        super().__init__(emp_name, salary)
        self.bonus=bonus
    def total_salary(self):
        return self.salary+self.bonus
print("--Employee Details--")
e1=Employee("Nicky",65000)
e1.display_details()
print("--Manager Details--")
m1=Manager("Nikhil",100000,15000)
m1.display_details()
print(f"Bonus : {m1.bonus}")
print(f"Total Salary : {m1.total_salary()}")