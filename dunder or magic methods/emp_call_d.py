class Emp:
    def __call__(self,name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __str__(self):
        return f"Name:{self.name}\nAge:{self.age}\nSalary:{self.salary}"
e1=Emp()
e1("Nikhil",21,400000)
print(e1)
# Output:
# Name:Nikhil
# Age:21
# Salary:400000