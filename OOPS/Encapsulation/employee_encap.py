# 4.Design an Employee class where:
# • salary is hidden
# • outsiders cannot read salary directly
# • use getter method that logs each access attempt
# • provide a method to update salary but only if the new salary is higher (prevent
# accidental downgrade) 

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        print("Salary accessed")
        return self.__salary
    def update_salary(self,new_salary):
        if new_salary>self.__salary:
            self.__salary=new_salary
        else:
            print("Cannot reduce salary")
e=Employee("Nikhil",50000)
print(e.get_salary())
e.update_salary(60000)
print(e.get_salary())
e.update_salary(40000)