#coding:utf-8
'''
import os
支持linux/unix系统
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
from multiprocessing import Process,cpu_count
import os
import time
num_cpus = cpu_count()
print num_cpus,'hello world'
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    # print('Parent process id ppid %s'%(os.getpgid()))
    time.sleep(10)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
