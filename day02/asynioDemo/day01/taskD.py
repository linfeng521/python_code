import asyncio
import time


now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
# task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态
# 在task加入事件循环之前为pending状态，当完成后，状态为finished
# asyncio.ensure_future(coroutine)创建task
task = loop.create_task(coroutine)
print(task) #  待定；悬而不决
loop.run_until_complete(task)
print(task)
print("Time:",now()-start)