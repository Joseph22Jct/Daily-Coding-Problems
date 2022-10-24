# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import asyncio

async def JobScheduler(func, ms):
    await asyncio.sleep(ms/1000)
    print(func)
    func()
    pass

def job():
    print("Hello World")

def main():
    asyncio.run(JobScheduler(job, 1000))
    pass

if __name__ == "__main__":
    main()