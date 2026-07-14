# Create a class Member that:
# •	Has a shared BMI limit for “fit” status.
# •	Each member stores name, height, weight.
# •	Has a method to calculate BMI and check fit status.
# •	Provides a function to update BMI limit for all members.
# •	Offers a tool to check if height and weight entered are valid numbers.
# Demonstrate:
# 1.	Creating multiple members.
# 2.	Updating BMI standard.
# 3.	Displaying fit status and input validity.

class Member:
    bmi_limit=25
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

    def bmi(self):
        return self.weight / (self.height**2)

    def fit_status(self):
        return self.bmi() <= Member.bmi_limit

    @classmethod
    def update_limit(cls,new_limit):
        cls.bmi_limit = new_limit

    @staticmethod
    def is_valid_input(height, weight):
        return (isinstance(height, (int, float)) and height > 0 and
                isinstance(weight, (int, float)) and weight > 0)

m1 = Member("Nikhil", 1.75, 70)
m2 = Member("Nicky", 1.65, 85)

print(m1.name, "BMI:", round(m1.bmi(), 2), "Fit?", m1.fit_status())
print(m2.name, "BMI:", round(m2.bmi(), 2), "Fit?", m2.fit_status())

Member.update_limit(27)

print(m1.name, "Fit after update?", m1.fit_status())
print(m2.name, "Fit after update?", m2.fit_status())

print("Valid input?", Member.is_valid_input(1.8, 75))
print("Valid input?", Member.is_valid_input(-1.8, 75))