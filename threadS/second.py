import threading
import time
start_time = time.time()
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg=arg
    def run(self):
        time.sleep(3)
        print(threading.current_thread().getName())
        print('the arg is: %s\n'%self.arg)

threads = []
for i in range(4):
    t = MyThread(i)
    threads.append(t)

for i in threads:
    i.start()

for i in threads:
    i.join()

print('main thread end')
print('花费时间: %s'%(time.time()-start_time))