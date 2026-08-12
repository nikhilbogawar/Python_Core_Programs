# Inheritance:-> it contains child class and parent class
# MRO: Method Resolution Order

#example: simgle level inheritance:->
# class Users:
#     def __init__(self,name,dob):
#         self.name=name
#         self.dob=dob
#     def login(self):
#         print("Login successfully")
#     def logout(self):
#         print("logout successfully")
# u1=Users("Nikcy","16-01-2005")
# u1.login()
# u1.logout()
# class Students(Users):
#     def exams(self):
#         print("Exams attended")
# s1=Students("Nikhil","15-01-2005")
# s1.exams()
# s1.login()
# s1.logout()
#-------------------------------------------------------------------------
# Multiple inheritance:->
# we can use multiple inheritances

# users  class-----------------
#                             \/
# another  class ------------->  main
#                             /\
# another class----------------
# example:->
class Plans:
    def m1(self):
        print("plans class")
class Airtel(Plans):
    def m2(self):
        print("airtel 5g")
class Customer(Airtel):
    def m3(self):
        print("Hii")

#--------------------------------------------------------------------------
# hierarchical inheritance:->
#        user
#      /      \
# airtel        jio
#-----------------------------------------------------------------------------
# hybrid inheritance:->
# user       plans        payments
#     \    /      \  __/  /
#       \/     ____/\    /
#     airtel /       jio       # airtel have user, plans and payments and jio also have user, plans, and payments
#            \       /
#            customer