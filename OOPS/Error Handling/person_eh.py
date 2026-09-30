# • Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0
class Person:
    def __init__(self,age):
        if age<0:
            raise ValueError("Age cannot be less than 0")
        self.age=age
try:
    p=Person(-5)
except ValueError as e:
    print(e)