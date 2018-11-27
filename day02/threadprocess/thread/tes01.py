#coding:utf-8
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t2 = threading.Thread(target=loop, name='LoopThread02')
'''
t2.start()
t2.join()
t.start()
t.join()
线程02先运行完，后线程1才能运行
'''
t.start()
t2.start()
t.join()
t2.join()
# 线程t和t2交替执行
print('thread %s ended.' % threading.current_thread().name)