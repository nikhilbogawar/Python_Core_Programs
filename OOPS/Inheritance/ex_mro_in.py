class A:
    def m1(self):
        print('A class')
        super().m1()
class B:
    def m1(self):
        print("B class")
class C(A,B):
    def m1(self):
        print("C class")
        super().m1()       # we can write as super(C,self).m1()
print(C.mro())
print(B.mro())
print(A.mro())
c1=C()
c1.m1()