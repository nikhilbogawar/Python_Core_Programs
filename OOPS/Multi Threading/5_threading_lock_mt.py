# 5. Modify the previous program so that the shared variable counter is updated
# in a thread-safe manner using threading.Lock, and ensure that the final printed
# value of the counter is always correct.

import threading
c=0
l=threading.Lock()
def increment():
    global c
    for i in range(10000):
        with l:
            c+=1
t1=threading.Thread(target=increment)
t2=threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Final Counter Value : {c}")