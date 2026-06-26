import asyncio

async def worker():
    print("Start")
    await asyncio.sleep(1)
    print("Done")

async def main():
    await worker()

worker()

asyncio.run(main())