# 介绍了——函数的函数__closure__--属性
value1 = 5
'''
在一个外函数中定义了一个内函数，
内函数里运用了外函数的临时变量，
并且外函数的返回值是内函数的引用。
这样就构成了一个闭包。
'''
def my_func():
    value2 = 6
    value3 = 10
    print('value2的id值是： %#x' % id(value2)) #打印value2的ID值
    print('value3的id值是： %#x' % id(value3))
    def in_func():
        a = max(value1, value2)
        print('value2的id值是： %#x'%id(value2))
        print('value3的id值是： %#x'%id(value3))
    return in_func

f = my_func()    #my_func返回的是in_func，此时f指向in_func函数
print(f.__name__) # >>out:in_func
f()    #f()相当于in_func()，调用了infunc函数
print(f.__closure__)
'''
如果内部函数引用了enclosing作用域的变量，会将变量添加到函数__closure__的属性中去。
当再次查找这个变量时，会直接去函数__closure__的属性中查找。
可以看到代码的输出结果第一行即为value2的内存地址转换为16进制
'''