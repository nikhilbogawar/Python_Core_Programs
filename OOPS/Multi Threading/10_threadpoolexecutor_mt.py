# 10. Write a Python program using ThreadPoolExecutor with three worker threads
# that submits tasks to compute the square of numbers from 1 to 5 and prints each
# result as soon as the corresponding task completes.

import threading
from concurrent.futures import ThreadPoolExecutor
import time

def fun(x):
    print(f"Thread starting {x}")
    time.sleep(5)
    return x*x

with ThreadPoolExecutor(max_workers=3) as e:
    # result=e.map(fun,range(1,6))
    result=[e.submit(fun,y) for y in range(1,6)]
    for i in result:
        print(i.result())