class Test(object):
    ID = 1

    def __init__(self):
        pass

    def prtID(self):
        print(self.ID)

    def classplusOne(self):
        Test.ID += 1
        print(Test.ID)

    def ObjplusOne(self):
        self.ID += 1
        print(Test.ID)


t1 = Test()
t2 = Test()
t1.prtID()
t1.classplusOne()  # 此时t1的操作会影响t2中的ID的值,说明ID是类中的变量而不是实例中的变量
t2.prtID()
t2.ObjplusOne()


# 如果把上面函数中的Test.ID 换成self.ID则输出的Test.ID永远是1,不会被改变如下:
class Test1(object):
    ID = 1

    def __init__(self):
        pass

    def prtID(self):
        print(self.ID)

    def classplusOne(self):
        self.ID += 1
        print(Test1.ID)
        print(self.ID)  # 这里输出的是2

    def ObjplusOne(self):
        self.ID += 1
        print(Test1.ID)
        print(self.ID)  # 这里输出的是2


t1 = Test1()
t2 = Test1()
t1.prtID()
t1.classplusOne()  # 此时t1的操作会影响t2中的ID的值,说明ID是类中的变量而不是实例中的变量
t2.prtID()
t2.ObjplusOne()

