import time
import threading

num = 0


class MyThread(threading.Thread):
    def run(self):
        lock.acquire()
        time.sleep(0.1)
        global num
        num += 1
        print(self.name + 'set num to ' + str(num))
        lock.release()

lock = threading.RLock()
threads = []
for i in range(100000):
    t = MyThread()
    threads.append(t)
for i in range(100000):
    threads[i].start()
print(threading.current_thread().getName())
print(threading.activeCount())
for i in range(10000):
    threads[i].join()