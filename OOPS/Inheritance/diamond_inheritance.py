# diamond shape inheritance like a method chaining
class A:
    def m1(self):
        print('A class')
        super().m1()
class B(A):
    def m1(self):
        print("B class")
        super().m1()
class C(A):
    def m1(self):
        print("C class")
        super().m1()
class E:
    def m1(self):
        print('E class')
class F(E):
    def m1(self):
        print("F class")
        super().m1()
class D(B,C,F):
    def m1(self):
        print("D class")
        super().m1()

print(D.mro())  # D,B,C,A,F,E,Obj
# like a method chaining
d1=D()
d1.m1()
# output:
# D class
# B class
# C class
# A class
# F class
# E class