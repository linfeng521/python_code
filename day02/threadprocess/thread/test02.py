#coding:utf-8
import threading
'''
在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)
    
def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)
    
def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
每个函数一层一层调用都这么传参数那还得了？用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。
'''
# 用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象
'''
global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
'''
import time
start_time = time.ctime()
# 创建全局ThreadLocal对象,但每个线程都只能读写自己线程的独立副本
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s) excute in %s' % (std, threading.current_thread().name, time.ctime()))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    time.sleep(10)
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
# t1.join() # 主线程main处于阻塞状态
# t2.join()
end_time = time.ctime()
print start_time,end_time