import time
import functools
def timer(delay):
    def time1(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start=time.time()
            print("Started: ",start)
            time.sleep(delay)
            print(f"Sum: {func(*args, **kwargs)}")
            end=time.time()
            print(f"End:{end}")
            print("Time taken: ",end-start)
        return wrapper
    return time1
@timer(5)
def add(x,y):
    sum=0
    for i in range(1,x+y+1):
        sum=sum+1
    return x+y
add(100,200)
print(add.__doc__)
print(time.asctime())
print(list(time.asctime().split()))
# Output:
# Started:  1783493356.0342445
# Sum: 300
# End:1783493361.0351784
# Time taken:  5.000933885574341
# None
# Wed Jul  8 12:27:43 2026
# ['Wed', 'Jul', '8', '12:27:43', '2026']
