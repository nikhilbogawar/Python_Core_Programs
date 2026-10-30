# 4. Write a Python program where two threads increment a shared variable named
# counter exactly 100000 times each without using any synchronization mechanism,
# and print the final value of the counter to demonstrate inconsistent or
# incorrect results caused by a race condition.

import threading
c=0
def increment():
    global c
    for i in range(10000):
        c+=1
t1=threading.Thread(target=increment)
t2=threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Final Counter Value : {c}")