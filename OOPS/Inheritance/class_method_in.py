# Inheritance using class method
class A:
    @classmethod
    def m2(cls):
        print("Hello")
    @classmethod
    def m3(cls):
        print("Bye")
class B(A):
    @classmethod
    def m2(cls):
        super().m2()
        print("World")
        super().m3()       # we can write super(B,B()).m3()
b1=B()
b1.m2()
print("----------------------------------------------------")
# Inheritance using class method suing composition
class A:
    @classmethod
    def m2(cls):
        print("Hello")
    @classmethod
    def m3(self):
        print("Bye")
class B:
    @classmethod
    def m2(cls):
        print("World")
        a1=A()
        a1.m3()
b1=B()
b1.m2()