# create a Base class A with m1 and m2 methods and sub class B with m3 method.
# create a object for both the class and call the methods
# class A:
#     def m1(self):
#         print("hello m1")
#     def m2(self):
#         print("hello m2")
# class B(A):
#     def m3(self):
#         print("hello m3")
#
# d1=A()
# d2=B()
# d1.m1()
# d1.m2()
# d2.m3()
# d2.m1()
# d2.m2()


# Another Example:------->
class A:
    def m1(self):
        print("m1 is here")
class B:
    def m1(self):
        print("m1 is also here")
a=A()
b=B()
a.m1()
b.m1()