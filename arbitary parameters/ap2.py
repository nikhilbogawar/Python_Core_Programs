#  Write a function multiply_all(*args) that returns the product of all numbers passed.
def multiply_all(*args):
    mul = 1
    for i in args:
        mul = mul * i
    return mul
print(multiply_all(1,2,3,4))