from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return ClassmateIterator(self)

class ClassmateIterator(object):
    def __init__(self,obj):
        self.current = 0
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        if self.current < len(self.obj.names):
            ret = self.obj.names[self.current]
            self.current +=1
            return ret
        else:
            raise StopIteration

c1 = Classmate()
c1.add("张三")
c1.add("李四")
c1.add("王五")

print("是否可以迭代:",isinstance(c1,Iterable))

c2 = ClassmateIterator(12)

print("是否是迭代器:",isinstance(c2,Iterator))

for i in c1:
    print(i)
    time.sleep(2)
