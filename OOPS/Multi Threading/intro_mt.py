import threading
import time
# class WorkerThread(threading.Thread):
#     def run(self):
#         c=0
#         x=c
#         time.sleep(0.001)
#         c+=1
# threads=[]
# for i in range(100):
#     t=WorkerThread()
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()
# print("final threads")


# Race Conditions is which threads run simultaneously, they interrupt each other mid-calculation.
# Lock allows exactly 1 thread at a time
# semaphore allows a specific N number of threads at a time (A BoundedSemaphore(1) acts exactly like a Lock)


# s=threading.BoundedSemaphore(2)
# class Pro(threading.Thread):
#     def run(self):
#         c=0
#         with s:
#             x=c
#             time.sleep(1)
#             c=x+1
# for i in range(100):
#     print(i)
# obj=Pro()
# obj1=Pro()
# obj.start()
# obj1.start()
# obj.join()
# obj.join()
# print("finished threads")


# Daemon Threads is used because it cleans up temporary memory files in the file in the background and periodically saving
# a user's text draft every few seconds, and it sends heartbeats like sending a regular "I am still alive" ping to a network server.

class BackGroundMusic(threading.Thread):
    def run(self):
        for i in range(1,101):
            print(f"Background Music playing {i}")
            time.sleep(0.1)
t=BackGroundMusic()
t.daemon=True
t.start()
print("Starting to load to play music")
time.sleep(11)
print("Closed the Music")