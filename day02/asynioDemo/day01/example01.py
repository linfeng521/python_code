import asyncio
import time


now = lambda :time.time()


async def do_some_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# wait:Wait for the Futures and coroutines given by fs to complete.
# asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) ,前者接受一个task列表，后者接收一堆task。
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("Task ret:",task.result())

print("Time:",now()-start)