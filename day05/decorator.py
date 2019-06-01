# 装饰器语法糖:@dec
def dec(func):
    print('call dec')
    def in_dec(*arg):
        print('in in_dec')
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return in_dec
#注意: dec函数的位置, 声明之前定义
@dec #装饰器返回一个新的函数即in_dec, 之后in_dec被my_sum接收,即my_sum->(in_dec(包含真正逻辑功能my_sum))
# 结合function_clouser @dec 就类似于 1. my_sum = dec(my_sum)
def my_sum(*arg): # 2. my_sum = in_dec()
    print('in my_sum')
    return sum(arg)
@dec
def my_avg(*arg):
    return sum(arg)/len(arg)



if __name__ == '__main__':
   # pass #>>out : call dec
    print(my_sum(1,2,3,4,5)) # in in_dec >>in my_sum 15
    print(my_sum.__name__) #in_dec