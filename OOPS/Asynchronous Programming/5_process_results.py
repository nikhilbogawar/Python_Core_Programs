# 5.	Process Results as They Complete Problem
# Simulate three web requests with different delays. Use asyncio.as_completed() to process
# each response immediately when it finishes instead of waiting for all.
import asyncio
async def request(name,delay):
    await asyncio.sleep(delay)
    return f"{name} response"
async def main():
    tasks=[request("Google",3),
           request("YouTube",1),
           request("Instagram",2)]
    for t in asyncio.as_completed(tasks):             # used as_completed() to process each response immediately
        print(await t)
asyncio.run(main())