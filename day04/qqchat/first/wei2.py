# 考虑到程序的健壮性以及维护性
import uiautomator2 as u2
import time
from first.psw import userid,passwd

class System:
    def __init__(self,ipAddress):
        # 连接设备
        self.d = u2.connect(ipAddress)
        self.d.app_stop_all()
        self.start()
        # self.d.app_clear('com.tencent.mm')
        # # 运行wechat
        # session = self.d.session('com.tencent.mm')
        # if session.running():
        #     weixin = Weixin(session)
        # # 切换fastinput输入法
        # session.set_fastinput_ime(True)

    def start(self):
        # 判断屏幕锁屏状态 fasle->
        if not self.d.info.get('screenOn'):
            print('屏幕启动')
            self.d.screen_on()
            # 屏幕解锁
            self.d.swipe(0.8, 0.7, 0.8, 0.2)

        # 健康性检查
        # 在手机的屏幕上显示Toast
        self.d.toast.show('start running!!!')
        # 清空微信数据
        self.d.app_clear('com.tencent.mm')
    def runWeichat(self):
        session = self.d.session('com.tencent.mm')
        if session.running():
            return session

class Weichat:

    def __init__(self, session):
        self.session = session
        session.set_fastinput_ime(True)
        self.login(userid,passwd)
        # 订座系统
        self.start()
        time.sleep(10)

    # 微信登录操作
    def login(self,userid, passwd):
        session = self.session
        # 点击登录按钮
        session(resourceId="com.tencent.mm:id/e4g").click()
        # 输入手机号
        session(resourceId="com.tencent.mm:id/kh").set_text(userid)
        # 点击下一步
        session(resourceId="com.tencent.mm:id/axt", text="下一步").click()
        # 输入密码
        session(resourceId="com.tencent.mm:id/kh", instance=1).set_text(passwd)
        # 点击登录按钮
        session(resourceId="com.tencent.mm:id/axt", text='登录').click()
        time.sleep(5)
        # 判断悬浮窗口
        # if session(text='是').exists:
        #     print('hi')
        #     session(resourceId="com.tencent.mm:id/az_",text='是').click()
        session(resourceId="com.tencent.mm:id/az_", text='是').click()

    # 开始运行订座系统点击任务
    def start(self):
        session = self.session
        # 由于首次登录加载数据过慢,特进行判断元素是否存在
        # d(resourceId="com.tencent.mm:id/d7b", text="通讯录").wait(timeout=3000)
        if session(resourceId="com.tencent.mm:id/d7b", text="通讯录").wait(timeout=3000):
            session(resourceId="com.tencent.mm:id/d7b", text="通讯录").click()
        # 公众号:
        session(resourceId="com.tencent.mm:id/a5t").click()
        # 点击搜索"我去图书馆"
        session(resourceId="com.tencent.mm:id/jy").click()
        # 输入
        session(resourceId="com.tencent.mm:id/kh").set_text('我去图书馆')
        # 点击搜索结果
        session(className="android.widget.TextView", text="我去图书馆").click()  # 进入公众号界面
        # 点击座位
        session(resourceId="com.tencent.mm:id/amt", text="座位").click()
        # 没办法~进入浏览器界面
        time.sleep(5)
        session.click(0.861, 0.717)
        print('Congratulations!! Seat reservation successful')
        session.toast.show('Congratulations!! Seat reservation successful',2.0)
    # 订座完成工作结束收尾

    def end(self):
        session = self.session
        print('successful,system will exit')
        session.toast.show('successful,system will exit')
        session.set_fastinput_ime(False)
        session.close()
        session.app_clear('com.tencent.mm')

if __name__=='__main__':
    system = System('192.168.1.7')

    session = system.runWeichat()

    weichat = Weichat(session)

