import vthread
import time
pool_1 = vthread.pool(5,gqueue=1) # open a threadpool with 5 threads named 1
pool_2 = vthread.pool(2,gqueue=2) # open a threadpool with 2 threads named 2

@pool_1
def foolfunc1(num):
    time.sleep(1)
    print(f"foolstring1, test3 foolnumb1:{num}")

@pool_2
def foolfunc2(num):
    time.sleep(1)
    print(f"foolstring2, test3 foolnumb2:{num}")

@pool_2
def foolfunc3(num):
    time.sleep(1)
    print(f"foolstring3, test3 foolnumb3:{num}")

for i in range(10): foolfunc1(i)
for i in range(4): foolfunc2(i)
for i in range(2): foolfunc3(i)
# default gqueue is 0