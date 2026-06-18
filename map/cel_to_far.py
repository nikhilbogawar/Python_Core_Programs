# celsius to farenhit using functions:
c=[0,-3,-8,2]
f=list(map(lambda x:((9*x/5)+32),c))
print(f)                 # [32.0, 26.6, 17.6, 35.6]

# def cel(x):
#     c=(x-32)*(5/9)
#     return c
# print(cel(29))