# 9.	Lock Synchronization Problem
# Create three coroutines trying to update the same shared account balance. Use asyncio.Lock() so only
# one coroutine updates the balance at a time.
import asyncio
balance=1000
async def update(amount,lock):
    global balance
    async with lock:
        balance+=amount
        print(f"Balance: {balance}")
        await asyncio.sleep(1)
async def main():
    lock=asyncio.Lock()
    await asyncio.gather(update(500,lock),update(300,lock),update(200,lock))
    print(f"Final Balance: {balance}")
asyncio.run(main())