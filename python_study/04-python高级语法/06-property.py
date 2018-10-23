class Student(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

if __name__ == "__main__":
    s = Student("小明",23)
    print(s.name,s.age)
