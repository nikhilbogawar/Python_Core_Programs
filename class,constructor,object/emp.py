# Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.

class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
# print("Before")
e1 = Employee("Nikhil")
e2 = Employee("Praveen")
e3 = Employee("Arjun")

print(e1.name, e1.company_name)
print(e2.name, e2.company_name)
print(e3.name, e3.company_name)

Employee.change_company("TCS")
# print("After")
print(e1.name, e1.company_name)
print(e2.name, e2.company_name)
print(e3.name, e3.company_name)

