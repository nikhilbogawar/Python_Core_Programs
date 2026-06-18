# farenhit to celsius using funcitons:
f=[0,-3,-8,2]
c=list(map(lambda x:(x-32)*(5/9),f))
print(c)            # [-17.77777777777778, -19.444444444444446, -22.22222222222222, -16.666666666666668]

# f=[0,-3,-8,2]
# def fun(x):
#     return (x-32)*(5/9)
# print(list(map(fun,f)))