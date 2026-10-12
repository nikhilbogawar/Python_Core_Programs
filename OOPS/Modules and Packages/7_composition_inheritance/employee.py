class Person:
    def display(self):
        print("Person details")
class Employee(Person):
    pass
class Laptop:
    def start(self):
        print("Laptop started")
class Developer:
    def __init__(self):
        self.laptop=Laptop()
    def work(self):
        self.laptop.start()