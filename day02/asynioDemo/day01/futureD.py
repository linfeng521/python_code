import time
import asyncio


now = lambda : time.time()


async def do_some_work(x):
    print("waiting:",x)
    return "Done after {}s".format(x)

# future: 代表将来它执行或没有执行的任务的结果。和task上没有本质上的区别
def callback(future):
    print("callback:",future.result())
    print(id(future))
# result: callback: Done after 2s


start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print(id(task)) # 和future的id值相同, 即是相同对象
print(task)
# <Task pending coro=<do_some_work() running at F:/ScrapyDemo/asynioDemo/day01/futureD.py:9>>
# 给task任务添加回调函数 task（也可以说是coroutine）执行完成的时候,就会调用回调函数
# 通过参数future获取协程执行的结果。这里我们创建 的task和回调里的future对象实际上是同一个对象
task.add_done_callback(callback)

print(task)
# <Task pending coro=<do_some_work() running at F:/ScrapyDemo/asynioDemo/day01/futureD.py:9>
#       cb=[callback() at F:/ScrapyDemo/asynioDemo/day01/futureD.py:14]>
loop.run_until_complete(task)

print("Time:", now()-start)