# def fun(x,y):
#     print(x+y)
#     return x*y
# def fun2(x:int,y:int) -> int:
#     print(x,y)
#     return x*y

def greet(name:str,age:int)->None:
    """Just experiment with functions"""
    print(f"Hello,{name}")
    print(f"age:{age}")
print(greet.__class__)  # <class 'function'>
print(greet.__name__)   # greet
print(greet.__doc__)    # Just experiment with functions
print(greet.__class__.__name__)   # function
print(greet.__class__.__name__)   # function
print(greet.__closure__)   # None
print(greet("Nikhil",21))  # Hello,Nikhil age:21 None

