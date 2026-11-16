# 10.	Producer–Consumer Queue Problem
# Build an async producer that adds 10 jobs into an asyncio.Queue, and two consumers
# that process the jobs concurrently. Use queue.join() and cancel consumers after all jobs are done.
import asyncio
async def producer(q):
    for i in range(1,11):
        await q.put(i)
async def consumer(q):
    while True:
        job=await q.get()
        print(f"Processing: {job}")
        await asyncio.sleep(1)
        q.task_done()
async def main():
    q=asyncio.Queue()
    c1=asyncio.create_task(producer(q))
    c2=asyncio.create_task(consumer(q))
    await c1
    await q.join()
    c1.cancel()
    c2.cancel()
    await asyncio.gather(c1,c2,return_exceptions=True)
    print("All jobs completed")
asyncio.run(main())