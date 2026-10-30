# 6. Write a Python program where one thread prints “A started” and then sleeps
# for two seconds, another thread prints “B started”, and the execution order is
# controlled in such a way that the second thread starts only after the first
# thread has completely finished.

import threading
import time
def task_a():
    print("A Started")
    time.sleep(2)
    print("A Finished")
def task_b():
    # time.sleep(2)
    print("B Started")
t1=threading.Thread(target=task_a)
t2=threading.Thread(target=task_b)
t1.start()
t1.join()
t2.start()
t2.join()
# time.sleep(1)
print("Main Thread Finished")