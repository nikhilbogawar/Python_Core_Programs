# Can a lambda function call another function inside it? Write an example.
def add(x,y):
    return x+y
double=lambda a,b: add(a,b)*2
print(double(44,78))
print(add(44,78))