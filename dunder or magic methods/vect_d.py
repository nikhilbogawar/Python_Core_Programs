class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __sub__(self, other):
        x=self.x-other.x
        y=self.y-other.y
        return Vector(x,y)
v1=Vector(10,15)
v2=Vector(7,8)
v3=Vector(9,17)
v4=v1+v2+v3
print(f"{v4.x,v4.y}")   # (26, 40)
v5=v4-v1-v2-v3
print(f"{v5.x,v5.y}")   # (0, 0)a