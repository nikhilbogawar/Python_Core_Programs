# while passing arguments must should pass only integer and no other datatype should pass
def valid(func):
    def inner(x,y):
        if isinstance(x,int) and isinstance(y,int):
            print(f"multiplying {x} and {y} is:",end=" ")
            func(x,y)                # multiplying 3 and 5 is: 15
        else:
            print("Arguments must be Integers")
    return inner
@valid                               # multiply=valid(multiply)
def multiply(x,y):
    print(x*y)
multiply(3,5)                  # passing arguments