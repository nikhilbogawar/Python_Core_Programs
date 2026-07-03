# def fun(a,b):
#     def fun2():
#         print("hello")
#         print(a*b)
#     return fun2()
# k=fun(10,20)
# k()
# print(k.__closures__[0].cell_contents)

#counts using closures
# def fun():
#     counts=0
#     def fun2():
#         nonlocal counts
#         counts+=1
#         print(counts)
#     return fun2
# x=fun()
# x()
# x()
# k=fun()
# k()

#functional reference
# def fun():
#     def fun2():
#         print("Hello")
#     return fun2
# k=fun()
# k()

# multiples suing closures
# def multiplier(x):
#     def inner(a):
#         return a*x
#     return inner
# x=multiplier(3)
# y=multiplier(5)
# print(x(30))
# print(y(25))
# print(x.__name__)

#----------------------

