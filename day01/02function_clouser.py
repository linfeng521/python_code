#coding:utf-8

def my_sum(*arg):
    print('in my_sum')
    return sum(arg)
def my_avg(*arg):
    return sum(arg)/len(arg)

def dec(func):
    def in_dec(*arg):
        print('in in_dec')
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return in_dec

if __name__ == '__main__':
    print my_sum.__name__ # my_sum
    print type(my_sum)    # <type 'function'>
    print my_sum(1,2,3,4,5) #in my_sum 15
    # dec return in_dec ->my_sum: 类似于java中的代理模式:演员-签约公司
    my_sum = dec(my_sum)
    print my_sum.__name__ #in_dec
    print my_sum(1,2,3,4,5) #in in_dec in my_sum 15







