from tasks import add
import time

result = add.delay(4,10)
print(result.ready())
time.sleep(1)
print(result.state)
print(result.get())
print(result.successful())
