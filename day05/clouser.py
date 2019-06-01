'''
在一个外函数中定义了一个内函数，
内函数里运用了外函数的临时变量，
并且外函数的返回值是内函数的引用。
这样就构成了一个闭包。
'''
#coding:utf-8
# __closure__作为一个值数据对象传递
def f_100(val):
    passline = 60
    if val > passline:
        print('pass')
    else:
        print('failed')

def f_150(val):
    passline = 100
    if val > passline:
        print('f_150 pass')
    else:
        print('f_150 failed')

def set_passline(passline):
    print('%x'%id(passline))
    def cmp(val):
        # passline引用了enclosing域中的passline变量, 所以将passline添加进cmp函数中__closure__属性中.
        #  因为passline变量计数为2, 函数执行完为1
        if val>passline:
            print('cmp pass')
        else:
            print('cmp faled')
    return cmp

if __name__ == '__main__':
    f_100 = set_passline(60)
    print(type(f_100))
    print(f_100.__closure__)
    print(dir(f_100))
    print(f_100.__name__)
    f_100(89)
    f_150 = set_passline(150)
    f_150(89)
    print(f_150.__name__)
    print(f_150.__call__.__name__)