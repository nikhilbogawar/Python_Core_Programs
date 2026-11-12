# 1.	Task Scheduling Problem
# Write an asyncio program where two API calls take different times to complete. Use asyncio.create_task()
# so both start immediately, and print which task finishes first.

import asyncio
from asyncio import create_task
async def api_call(name, delay):
    print(name, "started")
    await asyncio.sleep(delay)
    print(name, "completed")
    return name
async def main():
    task1=create_task(api_call("API 1",3))
    task2=create_task(api_call("API 2",1))
    await asyncio.gather(task1,task2)
asyncio.run(main())