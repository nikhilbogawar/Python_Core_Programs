# l=[1,2,[3,4]]
# import copy
# k = copy.deepcopy(l)
# from copy import deepcopy    # deep copy
# k = deepcopy(l)
# k[2].append(37)
# print(l)
# print(k)
# ------------------------------------------------------------------------
# k=l.copy()
# k[2].append(35)            # shallow copy
# print(l)
# print(k)
# ------------------------------------------------------------------------
# functions in python:

# def func(x):
#     print(x**x)
# func(3)
# ------------------------------------------------------------------------
# def details(name, age, branch):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Branch: {branch}")
# details(name="Nikhil", age=21, branch="CSE")
# ------------------------------------------------------------------------
# x=300
# def func4():
#     print(x)     #unbound local error
#     x=200
# func4()
# ------------------------------------------------------------------------
# def func5(x,y):
#     print("Sum of x:",sum(x))
#     print("Sum of y:",sum(y))
#     print("Sum of x and y:",sum(x)+sum(y))
# func5([1,2,3,4,5], [6,7,8,9,10])
# ------------------------------------------------------------------------
# Arbitary parameters in python:

# def func6(*args):
#     print(args)                               #Positional arguments
#     print(*args)                              #Unpacking the arguments
# func6(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# ------------------------------------------------------------------------
# def func7(**kwargs):
#     print(kwargs)                             #Keyvalue arguments
# func7(a=10, b=20, c=30, d=40, e=50)
# ------------------------------------------------------------------------
# def func8(a,b):
#     print(a,b)
# def func9(**kwargs):
#     print(kwargs)
#     func8(**kwargs)                             #Unpacking the keyvalue arguments
# func9(a=10, b=20)
# ------------------------------------------------------------------------
# def func10(*args, **kwargs):
#     print(args,kwargs,sep="\n")                                          #tuple
#     print(type(args), type(kwargs), sep="\n")                            #dicitonary
# func10(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,a=10,b=20,c=30,d=40,e=50,f=60)
# ------------------------------------------------------------------------
# def func11(*a):
#     s=0
#     for i in a:
#         s+=i
#     print(s)
# func11(7,8,6,5,2,3,9)
# ------------------------------------------------------------------------
# def func11(*a):
#     s=1
#     for i in a:
#         s*=i
#     print(s)
# func11(7,8,6,5,2,3,9)
# ------------------------------------------------------------------------
# return statement in python:
# def func12(a,b):
#     print(a+b)
#     return a+b
# print(func12(10,20))
# ------------------------------------------------------------------------
# def func13(a,b):
#     return a*b
# def func14(x,y):
#     return x+y
# print(func14(func13(23,53), func13(31,27)))    #2056 answer
# ------------------------------------------------------------------------
# question: f(x)= x^3 + 3x^2 + 53  g(y)= y^2 +2y + 1   v(x,y) : x*y  for this print(v(f(10),g(12)))
# def f(x):
#     return x*3 + 3*x*2 + 53
# def g(y):
#     return y**2 + 2*y + 1
# def v(x,y):
#     return x*y
# print(v(f(10),g(12)))         #228657 answer
# ------------------------------------------------------------------------
# a=5
# def f():
#     global a
#     a+=1
#     print(a)
# f()   #6
# ------------------------------------------------------------------------
# a=5
# def f():
#     a+=1
#     print(a)   #unbound local error
# f() 
# ------------------------------------------------------------------------
# memory management in python: threshold, count, referents, referrers, disable, enable
# import gc
# gc.collect()
# a = ["Hello", "Hi", 6000]
# # print(gc.get_referrers(10)) 
# print(gc.get_referents(a))
# print(gc.get_count())
# print(gc.get_threshold())
# print(gc.set_threshold(700,10,10))
# print(gc.get_threshold())
# print(gc.disable())
# print(gc.enable())
# --------------------------------------------------------------
#  Write a function called say_hello() that prints 'Welcome to Python!' 
# def say_hello():
#     print('Welcome to Python!')
# say_hello()
# ----------------------------------------------------------
#  Write a function called add(a, b) that returns the sum of two numbers. 
# def funcsum(a,b):
#     return a+b
# print(funcsum(12,20))
# ------------------------------------------------------------
#  What is the output of a function that has no return statement? Write a function to verify this.
# def func():
#     print("This function has no return statement.")
# func()
# ----------------------------------------------------------
#   Write a function area_of_rectangle(length, width) that returns length * width. Call it with values 6 and 4. 
# def rec(length, width):
#     return length * width
# print(rec(6,4))
# ---------------------------------------------------------
#  Create a function describe_pet(animal, name) that prints: 'My [animal] is named [name].' 
# def describe_pet(animal, name):
#     print(f"My {animal}'s name is {name}.")
# describe_pet('Lion', 'Simba')
# -----------------------------------------------------------
# What happens if you call a function with fewer arguments than parameters? Try it and note the error. 
# def func(a,b):
#     return a+b
# print(func(10))  #TypeError: func() missing 1 required positional argument: 'b'
# -------------------------------------------------------
#  Write a function power(base, exponent) that returns base raised to exponent using the ** operator. 
# def func(base, exponent):
#     return base ** exponent
# print(func(4, 6))
# ------------------------------------------------------------
#   Create a function full_name(first, middle, last) that returns the full name as a single string. 
# def full_name(first_name, middle_name, last_name):
#     return f"{first_name}{middle_name}{last_name}"
# print(full_name("Nikhil ", "Tejas ", "Bogawar"))
# --------------------------------------------------------------