# Q3. Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y)
        elif isinstance(other,int):
            self.x+=other
            self.y+=other
            return self
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return f"Vectors:{self.x,self.y}"
v1=Vector(2,5)
v2=Vector(7,9)
v3=Vector(10,1)
print(v1+v2+v3)