import uiautomator2 as u2
import time
# 定义一个名为Music的class类，用于存放所有Music的相关点击、组合等操作
class Music:
    def __init__(self,d):
        self.d = d
        print('设备'+self.d.info['productName']+'成功连接')
    # 启动网易云app packageName: com.netease.cloudmusic
    def start(self):
        self.d.app_start('com.netease.cloudmusic')
        time.sleep(2)
    # 点击播放按钮d(resourceId="com.netease.cloudmusic:id/bbz")
        self.d(resourceId="com.netease.cloudmusic:id/bbz").click()
    def image(self):
        self.d(resourceId="com.netease.cloudmusic:id/acm", className="android.widget.ImageView", instance=3).click()
        self.d(resourceId="com.netease.cloudmusic:id/t4").click()
    def next(self):
        self.d(resourceId="com.netease.cloudmusic:id/tu").click()
    def play(self):
        self.start()
        self.image()
        self.next()
class System():
    def __init__(self,d):
        self.d = d
    # 判断屏幕状态
    def screen(self):
        # 如果屏幕关闭
        if not self.d.info['screenOn']:
            self.d.screen_on()
           # self.d.swipe() 滑动解锁
if __name__ == '__main__':
    d = u2.connect('192.168.1.7')
    music = Music(d)
    music.play()

