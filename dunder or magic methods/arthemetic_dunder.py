class A:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return self.x+other.x
    def __sub__(self, other):
        return self.x-other.x
    def __mul__(self, other):
        return self.x*other.x
a1=A(20)
a2=A(10)
print(a1+a2)  # 30
print(a1-a2)  # 10
print(a1*a2)  # 200