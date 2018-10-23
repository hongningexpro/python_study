class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.names):
            ret = self.names[self.current]
            self.current +=1
            return ret
        else:
            raise StopIteration

c1 = Classmate()

c1.add("张三")
c1.add("李四")
c1.add("王五")

for i in c1:
    print(i)
