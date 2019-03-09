import uiautomator2 as u2

import schedule
import time

def job():
    print("I'm working..."+time.ctime())

def me(name):
    print('hello'+time.ctime()+name)
schedule.every().second.do(job)
schedule.every().day.at("19:31").do(me,'linfeng')

while True:
    schedule.run_pending()
    time.sleep(1)