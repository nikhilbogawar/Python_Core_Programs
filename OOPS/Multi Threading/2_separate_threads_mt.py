# 2. Write a Python program that creates three separate threads where each thread prints numbers from 1 to 5,
# and every printed number must be prefixed with the name of the thread that printed it, such as “Thread-1: 3”.

import threading
def printing_no(name):
    for i in range(1,6):
        print(f"{name} : {i}")
t1=threading.Thread(target=printing_no,args=("Thread-1",))
t2=threading.Thread(target=printing_no,args=("Thread-2",))
t3=threading.Thread(target=printing_no,args=("Thread-3",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("All Threads Completed")