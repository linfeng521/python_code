import uiautomator2 as u2
import time
from first.psw import userid,passwd
class Weixin():

    def __init__(self,session):
        self.session = session
def login(userid,passwd,session):

    # 点击登录按钮
    session(resourceId="com.tencent.mm:id/e4g").click()
    # 输入手机号
    session(resourceId="com.tencent.mm:id/kh").set_text(userid)
    # 点击下一步
    session(resourceId="com.tencent.mm:id/axt",text="下一步").click()
    # 输入密码
    session(resourceId="com.tencent.mm:id/kh",instance=1).set_text(passwd)
    # 点击登录按钮
    session(resourceId="com.tencent.mm:id/axt", text='登录').click()
    time.sleep(5)
    # 判断悬浮窗口
    # if session(text='是').exists:
    #     print('hi')
    #     session(resourceId="com.tencent.mm:id/az_",text='是').click()
    session(resourceId="com.tencent.mm:id/az_", text='是').click()
    time.sleep(10)

def start(session):
    '''
    通讯录
    d(resourceId="com.tencent.mm:id/d7b", text="通讯录").click()
    公众号:
    d(resourceId="com.tencent.mm:id/a5t")
    点击搜索 "我去图书馆"
    d(resourceId="com.tencent.mm:id/jy")
    输入
    d(resourceId="com.tencent.mm:id/kh").set_text('我去图书馆')
    点击搜索结果
    d(className="android.widget.TextView",text="我去图书馆").click()# 进入公众号界面
    点击座位
    d(resourceId="com.tencent.mm:id/amt", text="座位").click()
    没办法~进入浏览器界面
    d.click(0.861, 0.717)
        '''
    # 点击通讯录
    session(resourceId="com.tencent.mm:id/d7b", text="通讯录").click()
    #公众号:
    session(resourceId="com.tencent.mm:id/a5t").click()
    #点击搜索"我去图书馆"
    session(resourceId="com.tencent.mm:id/jy").click()
    #输入
    session(resourceId="com.tencent.mm:id/kh").set_text('我去图书馆')
    #点击搜索结果
    session(className="android.widget.TextView", text="我去图书馆").click()  # 进入公众号界面
    #点击座位
    session(resourceId="com.tencent.mm:id/amt", text="座位").click()
    #没办法~进入浏览器界面
    time.sleep(5)
    session.click(0.861, 0.717)

def end(session):
    print('successful~~~~')
    time.sleep(10)
    session.close()
    d.app_clear('com.tencent.mm')

if __name__=='__main__':
    d = u2.connect('192.168.1.7')
    d.app_stop_all()
    d.app_clear('com.tencent.mm')
    # 运行wechat
    session = d.session('com.tencent.mm')
    if session.running():
        weixin = Weixin(session)
    # 切换fastinput输入法
    session.set_fastinput_ime(True)
    login(userid,passwd,session)
    start(session)
    # 关闭fastinput输入法
    session.set_fastinput_ime(False)
    time.sleep(100)
    end(session)

