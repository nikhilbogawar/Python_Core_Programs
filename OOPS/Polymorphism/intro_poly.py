# same obj same method -- method overloading
# example:-->>
class A:
    # def m1(self):
    #     print("A")
    # def m1(self,a):
    #     print("A",a)
    def m1(self,a=0,b=0):
        if a==0 and b==0:
            print("A")
        elif b==0:
            print("A",a)
        else:
            print(a+b)
obj=A()
obj.m1()