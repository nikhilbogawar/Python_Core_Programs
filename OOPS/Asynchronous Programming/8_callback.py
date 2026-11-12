# 8.	Callback Problem
# Create an async task that returns a calculated value. Attach a callback using add_done_callback() to print
# the result as soon as the task is completed.
import asyncio
async def calculate():
    print("callback started")
    await asyncio.sleep(1)
    return 10+20
def result(task):
    print(f"Result: {task.result()}")
async def main():
    task=asyncio.create_task(calculate())
    task.add_done_callback(result)
    await task
asyncio.run(main())