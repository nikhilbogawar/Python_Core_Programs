# 6.	Timeout Protection Problem
# Write a coroutine that simulates a slow database query. Use asyncio.wait_for() to cancel it
# if it takes more than 2 seconds, and print "Database timeout".
import asyncio
async def database():
    print("Database query started")
    await asyncio.sleep(5)
    return "Database result received"
async def main():
    try:
        res=await asyncio.wait_for(database(),timeout=2)
        print(res)
    except asyncio.TimeoutError:
        print("Database timeout")
asyncio.run(main())