import threading


# 返回当前的线程变量
print(threading.current_thread())
# 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
print(threading.active_count())
# 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
print(threading.enumerate())
def worker():
    print(threading.enumerate())
    print('{} say hello'.format(threading.current_thread().getName()))
    print('active_count: ',threading.active_count())

th1 = threading.Thread(target=worker,name='me_thread')
th2 = threading.Thread(target=worker,name='me02_thread')
# 开启线程
th1.start()
th1.join()
th2.start()
th2.join()
