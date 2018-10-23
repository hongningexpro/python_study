class Father(object):
    x = 1

class Son1(Father):
    pass

class Son2(Father):
    pass

print(Father.x,Son1.x,Son2.x)
Son1.x = 2
print(Father.x,Son1.x,Son2.x)
Father.x = 3
print(Father.x,Son1.x,Son2.x)
