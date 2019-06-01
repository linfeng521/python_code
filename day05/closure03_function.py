def my_sum(*args):
    return(sum(args))

def my_average(*args):
    return sum(args)/len(args)

def dec(func):
    def in_dec(*args):
        if len(args) == 0:    #对参数进行判断，如果没有参数直接返回0
            return 0
        for i in args:
            if not isinstance(i, int):    #对参数进行判断，如果有一个参数不是int类型，直接返回0
                return 0
        return func(*args)    #此处对enclosing作用域的func函数进行引用
    return in_dec

evo_my_sum = dec(my_sum)
evo_my_average = dec(my_average)
evo_my_sum(1, 2, 3)
'''
PS:此处求和函数(my_sum)和求平均值函数(my_average)只对参数是否int类型进行判断。
我们来分析下代码：evo_my_sum = dec(my_sum)
由于函数dec返回的是in_dec函数
所以evo_my_sum指向的是in_dec函数
=》evo_my_sum = in_dec
=》evo_my_sum(1, 2, 3) = in_dec(1, 2, 3)
那么in_dec(1, 2, 3)即evo_my_sum(1, 2, 3)会对求和的参数先进行判断后，再调用my_sum函数。
同样道理：
evo_my_average会对求平均的参数先进行判断后，再调用my_average函数。
这样就可以对参数统一进行判断后再各自调用不同的函数。
'''