# 两段代码都能正确判断满分是100或150时，分数是否及格。但是第二段代码，由于运用闭包，代码复用性更高。

# __closure__作为一个值数据对象传递
def func_100(value):
    passline = 60
    if value >= passline:
        print('pass')
    else:
        print('failed')

def func_150(value):
    passline = 90
    if value >= passline:
        print('pass')
    else:
        print('failed')
func_100(59)
func_150(89)

def set_passline(passline):
    def in_func(value):
        # passline引用了enclosing域中的passline变量, 所以将passline添加进cmp函数中__closure__属性中.
        #  因为passline变量计数为2, 函数执行完为1
        if value >= passline:
            print('pass')
        else:
            print('failed')
    return in_func
f_100 = set_passline(60) #passline=60被存储在f_100的__closure__属性中
f_150 = set_passline(90) #passline=90被存储在f_150的__closure__属性中
print(f_100.__closure__)
f_100(59)
f_150(89)
print(f_150.__name__)
print(f_150.__call__.__name__)