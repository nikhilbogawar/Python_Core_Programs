# 7. Write a Python program in which three worker threads wait until a
# synchronization signal is received, the main thread sleeps for two seconds and
# then signals all waiting threads using an event, after which each worker thread
# prints a message indicating that it has started execution.

import threading
import time
e=threading.Event()
def worker():
    print("hello")
    e.wait()
    print("end")
t1=threading.Thread(target=worker)
t2=threading.Thread(target=worker)
t3=threading.Thread(target=worker)
t1.start()
t2.start()
t3.start()
time.sleep(2)
e.set()
t1.join()
t2.join()
t3.join()
print("All Workers Finished")