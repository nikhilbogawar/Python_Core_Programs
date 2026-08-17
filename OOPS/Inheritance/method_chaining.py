# Method Chaining:--->
class A:
    def m1(self):
        print("A class")
class B(A):
    def m1(self):
        print("B class")
        super().m1()
class C(B):
    def m1(self):
        print("C class")
        super().m1()
class D(C):
    def m1(self):
        print("D class")
        super().m1()
d1=D()
d1.m1()