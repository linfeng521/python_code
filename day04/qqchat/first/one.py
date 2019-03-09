import uiautomator2 as u2
from time import sleep

d = u2.connect('192.168.43.77')

# 启动App
d.app_start("com.meizu.mstore")

sleep(10)