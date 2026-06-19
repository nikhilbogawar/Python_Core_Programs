# def func():
#     def func2():
#         print("Hello")
#     func2()
#     return func2
# FR=func()

def func(x,y):
    def func2(x):
        print(x+y)
    func2(x)
func(10,20)