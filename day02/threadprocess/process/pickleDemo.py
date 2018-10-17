#coding:utf-8
import pickle
'''
对象序列化：它是一个将任意复杂的对象转成对象的文本或二进制表示的过程。
同样，必须能够将对象经过序列化后的形式恢复到原有的对象。在 Python 中，这种序列化过程称为 pickle，
可以将对象 pickle 成字符串、磁盘上的文件或者任何类似于文件的对象，
也可以将这些字符串、文件或任何类似于文件的对象 unpickle 成原来的对象
'''
# pickle序列化对象 类似于json的操作
# pickle.dumps(src_obj,fileObject) 序列化
# pickle.loads() 反序列化

class MyPickle(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def dump(self, obj):
        """
        序列化对象
        :param obj:
        :return:
        """
        with open(self.file_name, 'ab') as f:
            pickle.dump(obj, f)
            print('dump data', obj.__dict__)

    def loaditer(self):
        """
        迭代反序列化对象
        :return:
        """
        f = open(self.file_name, 'rb')
        while True:
            try:
                obj = pickle.load(f)
                yield obj
            except EOFError:
                print('EOFError')
                f.close()
                print(f.closed)
                break


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))


aa = Person("aGood", 2)
bb = Person("bGood", 3)
cc = Person("cGood", 4)

p = MyPickle('c.txt')
p.dump(aa)
p.dump(bb)
p.dump(cc)

iter_obj = p.loaditer()
while True:
    try:
        print(next(iter_obj).__dict__)
    except StopIteration:
        print('stop')
        break
'''
run result:
('dump data', {'age': 2, 'name': 'aGood'})
('dump data', {'age': 3, 'name': 'bGood'})
('dump data', {'age': 4, 'name': 'cGood'})
{'age': 2, 'name': 'aGood'}
{'age': 3, 'name': 'bGood'}
{'age': 4, 'name': 'cGood'}
EOFError
True
stop
'''