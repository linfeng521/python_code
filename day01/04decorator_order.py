

def war1(func):
    print("这个是经纪人, 负责对外签约广告的")

    def inner_war1(*args,**kwargs):
        print("对这个公司进行评估ok?, 通知star接收")
        func(*args,**kwargs)
        print("获取广告收益")
    return inner_war1

def war2(func):
    print("这个是化妆师， 出门也要美美的")
    def inner_war2(*args,**kwargs):
        print("对star进行化妆, 哇, 好帅呀")
        func(*args, **kwargs)
        print("对star进行卸妆操作")
    return inner_war2

@war1
@war2
def f():
    print("待装饰的函数, 这个是star哦")

f()


