def func2(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

def func1(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

    func2(a,b,*args,**kwargs)

func1(1,2,3,4,5,6,name="xiaoming",age=21)
