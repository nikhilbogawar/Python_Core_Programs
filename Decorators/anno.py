import functools
def ann(func):
    @functools.wraps(func)            # wraps uses only attributes
    def inner(x,y):
        # print(func.__name__)
        # print(func.__annotations__)
        # print(func.__doc__)
        print(x,y)
        return func(x,y)
    return inner

@ann
def fun(a:int,b:int) -> int:
    """Just adding a Doc for the Function"""
    return a+b
print(fun(10,24))
print(fun.__name__)
print(fun.__annotations__)
print(fun.__doc__)