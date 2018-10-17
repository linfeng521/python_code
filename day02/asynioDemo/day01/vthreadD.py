import vthread
import time
now = lambda : time.time()
start = now()
print(now())
@vthread.pool(3) # just use this line to make pool, Create a threadpool with three threads
def crawl(i):
    import time;time.sleep(10) # Simulation time consuming
    print("crawl_url:",i)
    print(now())

urls = ["http://url1",
        "http://url2",
        "http://url3",
        "http://url4"]

for u in urls:
    crawl(u) # This function becomes a function that adds the original function to the thread pool.

print(now()-start)