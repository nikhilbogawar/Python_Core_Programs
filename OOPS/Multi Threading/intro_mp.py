# Multi Processing
import multiprocessing
import threading
import time
def fun1(name,y):
    print(f"started {name}")
    time.sleep(1)
    print(f"ended {name}")
def fun(x):
    print(f"hello from {x}")
    t1=threading.Thread(target=fun1, args=("thread1",1))
    t2=threading.Thread(target=fun1, args=("thread2",1))
    time.sleep(1)
    t1.start()
    t2.start()
    print("end...")
p1=multiprocessing.Process(target=fun, args=("process1",))
p2=multiprocessing.Process(target=fun, args=("process2",))
if __name__=="__main__":
    p1.start()
    p2.start()
    # p1.join()
    # p2.join() # we can use join also here....