# Basic Customizer Iterator
class A:
    def __init__(self,x):
        self.x=x
    def __iter__(self):
        return self
    def __next__(self):
        self.x+=1
        return self.x
a1=A(30)
l=iter(a1)  # l=a1   # a1.__iter__()   # A.__iter__(a1)     # Here no pointer will create
print(next(l))  # l.__next__()
# Output:------ 31