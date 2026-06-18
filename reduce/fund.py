funds = [1500, 2500, 1400, 1000, 3200]
def add(x,y):
    return x+y
from functools import reduce
print(reduce(add, funds))
print(reduce(lambda x,y: x+y, funds))  #using lambda function with reduce() function (only this line code)