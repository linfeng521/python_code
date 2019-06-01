import functools
'''
装饰器到这里还差最后一步：
my_sum函数经过装饰后，由于dec(my_sum)返回的是in_dec函数，此时my_sum.__name__属性将从‘my_sum’变成‘in_dec’，
为了保证此属性不变，需在in_dec函数定义前加上语句@functools.wraps(func)，保证my_sum.__name__属性不变。
否则，有些依赖函数签名的代码执行就会出错。一个完整的decorator的写法如下：
'''
def dec(func):
    @functools.wraps(func)
    def in_dec(*args):
        if len(args) == 0:
            return 0
        for i in args:
            if not isinstance(i, int):
                return 0
        return func(*args)
    return in_dec

@dec
def my_avg(*arg):
    return sum(arg)/len(arg)



if __name__ == '__main__':
    print(my_avg(1,2,3,4))
    print(my_avg.__name__)