# What is the error if you place a positional argument after a keyword argument? Test it. 
def fun(a,b,c):
    print(f"value of a,b,c: {a} {b} {c}")
fun(a=23, 5, 3)  #SyntaxError: positional argument follows keyword argument