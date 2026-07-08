import functools
import time
def tim(delay=3):
    def dec(fn):
        @functools.wraps(fn)
        def indec(*args, **kwargs):
            print(f"Just adding {delay}sec Delay to start the function")
            print(f"Address inside Decorator : {fn}")
            time.sleep(delay)
            result = fn(*args,**kwargs)
            print("Execution Completed")
            return result
        print(f"Address fn: {fn}")
        print(f"Address indec : {indec}")
        return indec
    return dec

k = int(input("Enter Delay : "))
@tim(k)
def add(a,b,c):
    """ Just adding A DOC"""
    return a+b+c
print(f"Address add : {add}")
print(add(10,15,25))
print(add.__doc__)
del k
# Output:
# Enter Delay : 2
# Address fn: <function add at 0x0000025BDDBBF950>
# Address indec : <function add at 0x0000025BDDEC5A60>
# Address add : <function add at 0x0000025BDDEC5A60>
# Just adding 2sec Delay to start the function
# Address inside Decorator : <function add at 0x0000025BDDBBF950>
# Execution Completed
# 50
# Just adding A DOC