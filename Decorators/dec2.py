def fun(x):
    def fun2():
        print(x)
        print(x.__name__)
        x()
    return fun2

# k = fun(fun3)
# k()
# print(k.__name__)
@fun
def fun3():
    print("World Hello")
# fun3 = fun(fun3)       # this line means @fun
fun3()