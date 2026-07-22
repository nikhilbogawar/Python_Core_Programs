class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return (self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return (self.x-other.x,self.y-other.y)
    def __mul__(self, other):
        return (self.x*other.x,self.y*other.y)
    def __truediv__(self, other):
        return (self.x/other.x,self.y/other.y)
    def __mod__(self, other):
        return (self.x%other.x,self.y%other.y)
v1=Vector(10,20)
v2=Vector(7,8)
print(v1+v2)   # (17,28)
print(v1-v2)   # (3, 12)
print(v1*v2)   # (70, 160)
print(v1/v2)   # (1.4285714285714286, 2.5)
print(v1%v2)   # (3, 4)