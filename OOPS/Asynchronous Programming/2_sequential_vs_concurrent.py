# 2.	Sequential vs Concurrent Execution Problem
# Create three coroutines that each take 2 seconds. First run them using normal await,
# then run them using asyncio.gather(). Compare total execution time.
import asyncio
import time
async def task():
    print("task started")
    await asyncio.sleep(2)
    print("task completed")
async def main():
    start=time.time()
    await task()
    await task()
    await task()
    print("sequential:",round(time.time()-start,2))
    start=time.time()
    await asyncio.gather(task(),task(),task())
    print("concurrent:",round(time.time()-start,2))
asyncio.run(main())