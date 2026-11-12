# 7.	Cancellation Problem
# Create a long-running background task like sending email notifications.
# Cancel it after 2 seconds and handle asyncio.CancelledError properly.
import asyncio
async def email():
    try:
        while True:
            print("Sending Email")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Email task cancelled")
async def main():
    task=asyncio.create_task(email())
    await asyncio.sleep(2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task stopped")
asyncio.run(main())