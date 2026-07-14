# Create an Employee class that:
# •	Keeps a minimum experience required for promotion (shared across all employees).
# •	Stores employee name, experience, and department.
# •	Has a method to check eligibility for promotion.
# •	Provides a function to update promotion criteria globally.
# •	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.	Creating employees from different departments.
# 2.	Changing promotion criteria.
# 3.	Displaying eligibility results and department validation.

class Employee:
    min_experience=3
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department

    def eligible_for_promotion(self):
        return self.experience >= Employee.min_experience

    @classmethod
    def update_criteria(cls,new_exp):
        cls.min_experience=new_exp

    @staticmethod
    def is_valid_department(dept):
        return dept in ["HR", "Tech", "Admin"]

e1 = Employee("Nikhil", 2, "Tech")
e2 = Employee("Nicky", 5, "HR")
print(e1.name, e1.eligible_for_promotion())  #False
print(e2.name, e2.eligible_for_promotion())  #True

Employee.update_criteria(2)
print(e1.name, e1.eligible_for_promotion())  #True
print(Employee.is_valid_department("Finance")) #Flase