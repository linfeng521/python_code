import asyncio
import time



now = lambda :time.time()

async def do_some_work(x):
    print("waiting:",x)
    # await 后面就是调用耗时的操作 利用asyncio.sleep(x)模拟耗时的Io操作
    # 网络请求，文件读取 协程的目的也是让这些IO操作异步化
    # await asyncio.sleep(x)，因为执行到这里sleep了，模拟了阻塞或者耗时操作，这个时候就会让出控制权。
    #  即当遇到阻塞调用的函数的时候，使用await方法将协程的控制权让出,以便loop调用其他的协程。
    # 就像生成器里的yield一样，函数让出控制权 协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print("Task ret:", task.result())
print("Time:", now() - start)