# super():--> this keyword is used when the function name is same for parent and child class to access only parent class,
# we use super keyword. and this is used inside class only.
class A:
    def m1(self):
        print("A class")
class B(A):
    def m1(self):
        print("B class")
        super().m1()
b1=B()
b1.m1()
# print(B.mro())

# Another Example:--->
class User:
    def order(self):
        print("Ordered Pasta")
class Restaurant(User):
    def order(self):
        super().order()
        print("Order Received")
class Zomato(Restaurant):
    def order(self):
        super().order()
        print("Delivery partner aligned")
z1=Zomato()
z1.order()
r1=Restaurant()
r1.order()