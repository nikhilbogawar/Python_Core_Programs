# create python application where we use 4 functions with parameters and return types call them in single line
add = lambda x: x + 5
sum = lambda x: x - 2
mul = lambda x: x * 4
div = lambda x: x / 2
final = add(sum(mul(div(99))))
print(final)          #201.0