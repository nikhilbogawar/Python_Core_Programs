# 9. Write a Python program that starts a daemon thread running an infinite
# loop which repeatedly prints “Running in background”, while the main thread
# sleeps for two seconds and then exits, and observe what happens to the daemon
# thread when the main program terminates.
import threading
import time
def fun():
    while True:
        print(f"Running in background {threading.currentThread().getName()}")
        time.sleep(0.5)
t1=threading.Thread(target=fun,daemon=True)
t2=threading.Thread(target=fun,daemon=True)
t1.start()
t2.start()
time.sleep(5)
print("Main Thread Ended")