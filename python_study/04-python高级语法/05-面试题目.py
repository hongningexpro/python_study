class Father(object):
    def __init__(self):
        self.x = 1

class Son1(Father):
    pass

class Son2(Father):
    pass

f = Father()
s1 = Son1()
s2 = Son2()
print(f.x,s1.x,s2.x)
s1.x = 2
print(f.x,s1.x,s2.x)
f.x = 3
print(f.x,s1.x,s2.x)
