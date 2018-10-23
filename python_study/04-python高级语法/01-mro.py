class Parent(object):
    def __init__(self):
        print("Parent init 开始")
        self.name = 1
        print("Parent init 结束")

class Son1(Parent):
    def __init__(self):
        print("Son1 init 开始")
        super().__init__()
        print("Son1 init 结束")


class Son2(Parent):
    def __init__(self):
        print("Son2 init 开始")
        super().__init__()
        print("Son2 init 结束")

class GrandSon(Son1,Son2):
    def __init__(self):
        print("GrandSon init 开始")
        super().__init__()
        print("GrandSon init 结束")

print(GrandSon.__mro__)

g1 = GrandSon()
