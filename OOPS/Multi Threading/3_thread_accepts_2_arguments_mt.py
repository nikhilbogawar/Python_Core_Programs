# 3. Write a Python program in which a thread accepts two integer arguments,
# computes their sum, prints the result from inside the thread, and ensures that
# the main thread waits until the worker thread completes execution.

import threading
def calculate_sum(a,b):
    result=a+b
    print(f"{sum} : {result}")
t1=threading.Thread(target=calculate_sum,args=(10,20))
t1.start()
t1.join()
print("Main Thread Completed")