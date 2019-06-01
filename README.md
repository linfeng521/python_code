# python_code

## discard  vt.	丢弃，抛弃; 解雇; 出牌;

## day05

重新学习python函数闭包和装饰器

___

> 装饰器是用来装饰函数的，它返回一个函数对象。增加`my_sum`函数的功能，比如，在函数调用前对参数进行一个判断，但又不希望修改`my_sum`函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

```
import functools

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
```

