# contains only oen thread
# like an event loop
# by using one thread we can use multiple tasks
# inside event loop it runs like a concurrent called tasks
# the tasks is called scheduling
# await it used inside the async def
# we should write the async before def
# inside the tread it contains event loop and inside the event loop it runs some tasks
# wait is used for tasks
# wait_for is used for 1coroutines

# import threading
# import asyncio

# import asyncio
# async def fun():
#     print("async prog")
#     await asyncio.sleep(1)
#     asyncio.run(fun1())        # co-routines | used to run the function we should write after completing the program
# async def fun1():
#     await fun()
#     await fun()

#
# async def basic_coroutine(name, delay):
#     print(f"[{name}] started on thread {threading.current_thread().name}")
#     await asyncio.sleep(delay)
#     print(f"[{name}] finished after {delay}s")
#     return name
#
# async def task_demo():
#     task1=asyncio.create_task(basic_coroutine("task1",5))
#     task2=asyncio.create_task(basic_coroutine("task2",1))
#     r2=0
#     r1=await task1
#     print("task results:",r1,r2)
#     r2=await task2
#     print(r2)

# in Gather and As_Completed we should send coroutines & it uses get_name | and in Wait we should send tasks.
# timeout_demo we should send coroutines & it contains wait-for.
# cancellation_demo is to create the task in coroutines.
# callbacks are used in big applications. after completing the task it prints callback result.
# locks are used if the task is running then the other task will not allow until the first task is completed.
# semaphores used when we want to allow limited as manually our-self. these semaphores are like locks.
# to thread locks, thread concurrency and all we use semaphores.
#
# async def main():
#     # await basic_coroutine("test",3)
#     # await basic_coroutine("test1",1)
#     await task_demo()
#
# if __name__=="__main__":
#     asyncio.run(main())