def dec(func):
    def inner(n):
        print("Starting this Function")
        print(func.__name__)     # greet
        func(n)
        print("Ending this Function")
    return inner

@dec
def greet(name):
    print(f"Hello {name}")
print(greet.__name__)          # inner
greet("Nikhil")