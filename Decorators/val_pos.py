#  Write a decorator called validate_positive that checks all positional arguments passed
# to a function. If any argument is negative, print an error message and return None without calling function. test it on function multiply(a,b
def validate_positive(func):
    def inner(a,b):
        if a<0 or b<0:
            print("Error: Negative Values are not allowed")
            return None
        else:
            func(a,b)
    return inner
@validate_positive
def multiply(a,b):
    print(a*b)
multiply(-5,3)
multiply(5,3)