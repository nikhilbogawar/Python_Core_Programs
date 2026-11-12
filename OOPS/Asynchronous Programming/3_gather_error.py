# 3.	Gather with Errors Problem
# Build three async tasks: two return data successfully and one raises an exception.
# Use asyncio.gather(..., return_exceptions=True) to collect all results without stopping the program.
import asyncio
async def task1():
    await asyncio.sleep(1)
    return "Data received 1"
async def task2():
    await asyncio.sleep(2)
    return "Data received 2"
async def task3():
    await asyncio.sleep(1)
    raise ValueError("Error occurred")
async def main():
    res=await asyncio.gather(task1(),task2(),task3(),return_exceptions=True)
    for r in res:
        if isinstance(r,Exception):
            print(f"Error: {r}")
        else:
            print(f"Success: {r}")
asyncio.run(main())