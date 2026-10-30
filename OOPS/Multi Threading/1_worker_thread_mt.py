# 1. Write a Python program that creates a worker thread which prints “Hello
# from worker thread” while the main thread prints “Hello from main thread”, and
# ensure that the main thread waits for the worker thread to finish execution
# before the program exits.

import threading
def worker():
    print("Hello from the worker thread")
t=threading.Thread(target=worker)
t.start()
print("Hello from main thread")
t.join()
print("Main thread finished")