import threading
import time
tickets = 10
'''
未引入锁
def shop(name):
    global tickets
    while True:
        if tickets > 0:
            time.sleep(3)
            print(name + ' shop one tickets and there stil has' + str(tickets-1))
            tickets = tickets-1
        else:
            break
ming shop one tickets and there stil has2
haha shop one tickets and there stil has1
ming shop one tickets and there stil has0
haha shop one tickets and there stil has-1

'''

lock = threading.Lock()
def shop(name):
    global tickets,lock

    while True:
        with lock: # with语句会在这个代码块执行前自动获取锁，在执行结束后自动释放锁
            if tickets > 0:
                time.sleep(3)
                print(name + ' shop one tickets and there stil has' + str(tickets-1))
                tickets = tickets-1
            else:
                break
'''
haha shop one tickets and there stil has3
ming shop one tickets and there stil has2
haha shop one tickets and there stil has1
ming shop one tickets and there stil has0
'''
threading_01 = threading.Thread(target=shop, args=('ming',), name='明星01')
threading_02 = threading.Thread(target=shop, args=('haha02',), name='菜鸟02')
threading_03 = threading.Thread(target=shop, args=('haha04',), name='菜鸟02')
threading_04 = threading.Thread(target=shop, args=('haha05',), name='菜鸟02')
threading_05 = threading.Thread(target=shop, args=('haha06',), name='菜鸟02')
threading_01.start()
threading_02.start()
threading_03.start()
threading_04.start()
threading_05.start()

