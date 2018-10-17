#coding:utf-8
# 进程间相互通信
# Python的multiprocessing模块包装了底层的机制,提供了Queue、Pipes等多种方式来交换数据。
# 队列是一种特殊的线性表，是一种先进先出（FIFO）的数据结构。它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作。
# 进行插入操作的端称为队尾，进行删除操作的端称为队头。队列中没有元素时，称为空队列。
from multiprocessing import Process, Queue
import os, time, random

# 父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据

# 写数据进程执行的代码:

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()