#  my_decorator(say_hello) is called. func = say_hello inside the decorator.
def my_decorator(func):
    def inner(n):
        func(n)
    return inner
@my_decorator
def say_hello(name):
    print(f"Hello {name}")
say_hello("Nikhil")