# 4.	Wait with Timeout Problem
# Create three tasks simulating file downloads: 1 sec, 3 sec, and 5 sec. Use asyncio.wait() with a timeout of 2 seconds.
# Print completed downloads and cancel pending ones.
import asyncio
async def download(n,delay):
    print(f"{n} started")
    await asyncio.sleep(delay)
    print(f"File {n} downloaded")
async def main():
    tasks=[asyncio.create_task(download(1,1)),
           asyncio.create_task(download(2,3)),
           asyncio.create_task(download(3,5))]
    done,pending=await asyncio.wait(tasks,timeout=2)
    print("Completed: ",len(done))
    for t in pending:
        t.cancel()
    await asyncio.gather(*pending,return_exceptions=True)
    print("pending tasks cancelled")
asyncio.run(main())