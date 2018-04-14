import os
import math


# 定义函数的语法
def hello(a):
    print(a)


hello("world")
hello(4)


# Definition function
def area(weight, height):
    return weight * height


def print_welcome(name):
    print("welcome", name)


print_welcome("wanyi")
w = 4
h = 5
print(area(w, h))


def printme(str):
    print(str);
    return;


printme("I need use the custom function")
printme("I need use twice")


# Transfer variable objects
def changeme(mylist):
    "Modifying the incoming list"
    mylist.append([1, 2, 3, 4])
    print("the value:", mylist)
    return


a = [10, 20, 30]
changeme(a)
print("the value2", a)


# Variable parameter
def printinfo(arg1, *vartuple):
    """Print any parameters that can be afferent"""
    print("Output:")
    print(arg1)
    for var in vartuple:
        print(var)
    return;


printinfo(12);
printinfo(10, 12, 14, 15);
print();

sum = lambda a, b: a + b;
print(sum(10, 20))
print()


# the return
# Writable function description
def sum(arg1, arg2):
    total = arg1 + arg2;
    print("function:", total)
    return total;


# Call function description
total = sum(10, 20)
print("the function2", total)

# Local variables and global variables
total1 = 0


def sum1(arg1, arg2):
    total1 = arg1 + arg2
    print("Local variables in a function", total1)
    return total1;


sum1(10, 20);
print("Function external is global variable", total1)

print()

# global and nonlocal
num = 1


def fun1():
    global num
    print(num + 2)
    num = 123
    print(num)


fun1()


def outer():
    num = 10

    def inner():
        nonlocal num
        print(num)
        num = 100
        print(num)

    inner()
    print(num)


outer()


def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist = [1, 2, 3, 4];
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
print(changeme(mylist))  # 在外层套一个print会输出一个none
print("函数外取值: ", mylist)

import builtins  # ？？？

print(dir(builtins))

# stack
print()
stack = [1, 2, 3]
stack.append(4)
stack.append(5)
print(stack)
print(stack.pop())  # ？？？
print(stack)

# tuples
print()
t = (1, 1, 2, 3)
print(t)
print(t[2])
u = t, (4, 5, 6)  # 两个元组组成元素
print(u)

# why?为什么用{}出来的是8346而用【】出来的是3648，---2月28，因为{}是集合，无序的，而[]是列表是有序的
print()
a = [x * y for x in range(1, 5) if x > 2 for y in range(1, 4) if y < 3]
print(a)

print()


#  2月28日  函数来自廖雪峰的博客
def absolute(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operated type')  # 输出错误的名称
    if x > 0:
        return x
    else:
        return -x


print(absolute(-9))


def nop():
    pass  # 空的语句站位，当想写的时候再写上


def ag():
    age = 0
    if age >= 18:
        pass


# # 一元二次方程求解函数
# a = input('请输入a')
# b = input('请输入b')
# c = input('请输入c')
#
#
# def quadratic(a, b, c):
#     """
#     :type a: object
#     """
#     if not a.isdigit() & b.isdigit() & c.isdigit():
#         raise TypeError('参数类型不是数字')
#     a, b, c = int(a), int(b), int(c)
#     if a == 0:
#         raise ValueError('参数不能为0')
#     deta = math.pow(b, 2) # 这个函数是什么意思
#     if deta < 0:
#         raise TypeError('没有实解')
#     else:
#         r1 = (-b + math.sqrt(deta)) / (2 * a)
#         r2 = (-b - math.sqrt(deta)) / (2 * a)
#         return r1, r2
#
# print(quadratic(a, b, c))

# 切片
L = ['a', 'b', 'c', 'd', 'e']
print(L[1:3])  # 包括前面不包括后面
print(L[-1])

L = list(range(100))
print(L[::5])


def trim(s):
    if s is None:  # 为什么s is None跟s==None不一样
        raise TypeError('没有输入参数')
    else:
        while s[:1] == '':
            s = s[1:]
        while s[-1:] == '':
            s = s[:-1]
        print('s')  # 这条语句当下面调用函数执行时才会执行，因为这个函数被调用了，所以执行到这，显示出了s
    # return s # 当return语句放在这的时候，表示函数已经执行完毕，下面的将不在执行，所以下面的print（A）不会执行
    print('A')  # 为什么这个print()函数没有任何输出???  ---自己解释-因为这个语句没有执行到，else语句结束后，函数就已经执行完了
    return s  # 当return语句放在这时，标志到这函数才会执行完毕，所以上面的A会输出


print(trim(' afghans '))

# 对于列表，既要遍历索引，又要遍历元素，使用enumerate更方便
list1 = ["这", "是", "一个", "简单", "测试"]
for i in range(len(list1)):
    print(i, list1[i])
print()
for a, b in enumerate(list1):
    print(a, b)
print()
for ind, ie in enumerate(list1, 1):  # enumerate接受第二个参数，用于指定索引的起始值
    print(ind, ie)


def findMaxMin(L):
    if len(L) == 0:
        return None, None
    max = min = L[0]

    for i in L:
        if max < i:
            max = i
        elif min > i:
            min = i
    return min, max


print(findMaxMin([12, 100, 23, 26, 67, 90]))  # 当列表里边不是数字时，而是字符串时，输出结果不对
# 字符串型的数字怎么比大小？？？



# 3月1号
# 列表生成器
L = []
for x in range(1, 11):
    L.append(x * x)
    print(L)  # 此语句会使每次的循环都会输出，且一次增加
print(L)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])  # 有if条件

print([m + n for m in 'ABC' for n in 'NML'])  # 全排列

print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录，os需要import

x = 123
print(isinstance(x, str))  # isinstance用来判断变量是什么类型

L = ['ABC', 'DEF', 9, 'GHI', 'KLM']
print([s.lower() for s in L if isinstance(s, str)])  # 条件用来判断是否是字符串，是的才转换

d = {'X': 'A', 'Y': 'B', 'Z': 'C'}  # 定义一个字典
for k, v in d.items():
    print(k, '=', v)

T = [k + '=' + v for k, v in d.items()]  # 列表生成式使用两个变量生成list
print(T)

print([s.lower() for s in T])  # 把列表中的大写字母换成小写字母

# 生成器
g = (x * x for x in range(10))  # （）代表的是生成器

print(next(g))  # 单个输出一个生成器中的值
print(next(g))

for n in g:  # generator也是可迭代对象，所以用for循环提取
    print(n)


# 简单的算法推算可以用列表生成式的for循环来实现，不能实现的时候用函数来实现

# 3月3日

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1  # 不用n=n+1
    return 'done'


# 此种斐波那契数列输出的为数列，可重复用性低

# # python中的循环语句，没有do......while...
# while 判断条件:
#     语句
# else：（while的条件为false时执行else后面的语句）

# for.....in....
#     语句
# else：
print(fib(8))


# 改进版斐波那契数列，输出的为列表，复用性高了，可是随着max增大，内存高，所以尽量不使用list来保存中间结果
# 只要是返回List类型的便会导致内存占用过大
def fib2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return L


print(x for x in fib2(8))  # 为什么比下面的程序多输出了一个generator对象

for y in fib2(7):
    print(y)

# 第三版斐波那契数列,把一个函数写成generator，由此获得了迭代能力，
# 如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
print()


def fib3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


for e in fib3(6):  # 这种for循环拿不到生成器的返回值，必须通过捕获stopiteration错误
    print(e)

g = fib3(9)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:  # 拿到返回值
        print('Generator return value:', e.value)
        break

from inspect import isgeneratorfunction

print(isgeneratorfunction(fib3))  # 判断一个函数是不是生成器，生成器实际返回一个generator对象


def odd():
    print('step1')
    yield (1)
    print('step2')
    yield (3)
    print('step3')
    yield (5)


o = odd()
next(o)
next(o)


# 杨辉三角，？？？？ 没弄明白？??/??
def triangles(i):
    a = [1]
    for n in range(i):
        yield a
        b = [1] + [a[m] + a[m + 1] for m in range(n)] + [1]
        a = b
    return 'done'


for a in triangles(4):
    print(a)
print()
# 3月4日
from collections import Iterable, Iterator

print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(100)), Iterable))
print(isinstance(100, Iterable))  # 数字不是可迭代对象

print()
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))  # 这种是迭代器对象，是一个数据流，

print(abs)  # 此时只是函数名
f = abs  # 函数本身也可以赋值给变量，即变量可以指向函数
print(f)
print(f(-10))

print()


def add(x, y, f):
    return f(x) + f(y)


f = abs
print(add(-5, 6, abs))


def f(x):
    return x * x


r = map(f, [1, 3, 5, 7, 9])  # map函数接受两个参数，一个是函数另一个是Iterable的参数例如列表，并把结果作为Iterator返回

print(list(r))  # 因为r是Iterator对象，所以可以用list进行返回

# 下面会出现跟map函数相同的作用，但是作用结果不明显
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

from functools import reduce


def add(x, y):
    return x + y


# reduce函数会将第二个参数列表依次放到第一个函数参数中，例如下面的例子，将返回求和，当然求和运算不用动用reduce，有sum（
print(reduce(add, [1, 3, 5, 7, 9]))

# 利用reduce函数写一个将字符串转换为整型的函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(isinstance(str2int('1234'), int))


def normalize(name):
    return print(name[0].upper() + name[1:].lower())  # 应为return的是print的，所以下面print（L）会出错
    # return name[0].upper() + name[1:].lower()  # 这是正确的


L1 = ['admin', 'jAck', 'ASDF', 'adjfiM']
L = list(map(normalize, L1))
print(L)

print()


# 3月5日
def is_odd(x):
    return x % 2 == 1


L = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(L))  # filter函数返回的是迭代器Iterator，所以用list获取所有结果并进行返回list


# 高阶函数的例子
def not_empty(x):
    return x and x.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '   '])))


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


for n in _odd_iter():  # 此时输出的为没有经过过滤的数列
    if n < 1000:
        print(n)
    else:
        break


def _not_divisiable(n):
    return lambda x: x % n > 0


def prim():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n), it)


for n in prim():
    if n < 1000:
        print(n)
    else:
        break

# sorted为排序函数
print(sorted([36, -12, 1, 23, 12]))
print(sorted([36, -12, 1, 23, 12], key=abs))
print(sorted([36, -12, 1, 23, 12], key=abs, reverse=True))
print(sorted(['abc', 'Zsw', 'bcf', 'Qaz'], key=str.lower, reverse=True))

# 对一个名字跟成绩构成的元组列表根据名字进行排序
L = [('Bob', 75), ('jack', 90), ('Rose', 76), ('Lisa', 80), ('Allen', 45)]


# 这里是定义一个key的规则，像abs一样，此处是返回
def by_name(t):
    return t[0].lower()


# 函数也是一个对象，而且函数对象可以被赋值给变量，函数对象有一个__name__属性，可以拿到函数的名字
print(by_name.__name__)

print(sorted(L, key=by_name))  # key指定的函数作用于L列表的每一个元组元素中，


def by_score(t):  # 将返回元组的第二个元素，成绩分数
    return t[1]


print(sorted(L, key=by_score))

# 用lambda匿名函数写返回奇数的表达式
L = list(filter(lambda x: x % 2 == 1, range(1, 30)))
print(L)

print()


# 3月6日

# 在python中，函数名加（），表示返回的是一个函数的结果，不加括号表示的是对函数的调用。？？？对不对
def log(func):
    def wrapper(*args, **kw):  # 这两个××kw有什么关系，修改一个，另一个会报错
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper  # 加括号跟不加括号什么区别？？


# 这里是返回的wrapper是函数对象，这个函数对象是在它内部定义的，在wrapper中调用了函数func，将func的调用结果作为值返回


@log
def now():
    print('2018-03-06')


now()
print(now)  # now是函数now的地址，而上面的now()为now方法,所以打印出now的的地址

# f = now
# print(f)



# 3月7日

# 偏函数
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
int()  # 此函数将字符串转换为整数
print(int('12345', base=8))
print(int('12345', base=16))

# print(int('2', base=2))

# def int2(x, base=2):
#     return int(x, base)
#

# print(int2('100000'))

import functools

int2 = functools.partial(int, base=2)  # functools.partial就是用来创建偏函数的，
print(int2('10101010110'))
print(int2('100000'))


def www(x, r=2, z=4):
    y = x + r + z
    return y


kw = {'r': 2, 'z': 4}
www1 = functools.partial(www, **kw)
a = www(1, 2, 4)
print(a)
b = www1(3)
print(b)

print()


# 3月10日
# 类    类可以看作是模块的子集
class Student(object):  # 类名称是大写字母开头
    pass


class Student(object):
    def __init__(self, name, score):  # 类中的函数第一个参数必须是self
        self.name = name
        self.score = score


jack = Student('jack', 60)
print(jack)  # 此时jack是一个类的实例
print(jack.name)
print(jack.score)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):  # 数据的封装
        print('%s:%s' % (self.name, self.score))

    def grade(self):  # 数据的封装可以给函数增加新的方法
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


Tom = Student('Tom', 90)
Tom.print_score()
print(Tom.grade())


# 加了访问限制的类
class Student(object):
    def __init__(self, name, score):
        self.__name = name  # 内部的__name变量其实已经把它切换成了_Student__name或者别的
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_name(self):  # 必须定义get方法来让外界可以访问
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):  # 通过定义的set方法进行修改
        if 0 < score < 100:  # 在这可以对输入的对象进行判断和检查
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_name(self, name):
        self.__name = name


Rose = Student('Rose', 89)
# print(Rose.__name) # 此时__name已经不能够被外界访问


print(Rose.get_name())  # 此时便可以通过内部定义的get方法进行访问
print(Rose.get_score())

# 通过get和set来实现访问限制的类,这样可以让内部的数据访问更合理

print()


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        # if gender == '男':  # 为什么此时把==换成is 就会出错,解释在下面
        #     self.__gender = gender
        # elif gender == '女':
        #     self.__gender = gender

        if gender == '男' or gender == '女':
            self.__gender = gender
        else:
            raise ValueError('请输入正确性别')


a = Student('Jordan', '男')
print(a.get_gender())

# print(a.gender) # 此时已经不能够进行访问gender参数


# a.set_gender('中')
a.set_gender('女')
a.set_gender('男')

print(a.get_gender())


#  Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。
# ==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等
# is也被叫做同一性运算符，这个运算符比较判断的是对象间的唯一身份标识，也就是id是否相同。



class Animal(object):
    def run(self):
        print('Animal is running....')


class Dog(Animal):
    def run(self):  # 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
        # 这样，我们就获得了继承的另一个好处：多态。
        print('Dog is running....')

    def eat(self):
        print('Eatting meat...')


dog = Dog()
dog.run()

# 多态是对扩展开放,对修改封闭

# 动态语言??
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

# 可以用type()判断的都可以用isinstance来判断
print(isinstance([1, 2, 3, 4], (list, tuple)))

# dir()函数,获得一个对象的所有属性和方法
print(dir(dog))
print(dir('abc'))  # 获的字符串的属性和方法

# 以下两种字符串是等价的,当调用len()函数时,其实就是调用了abc对象的__len()__方法
print(len('abc'))
print('abc'.__len__())


# 实例属性和类属性????



class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name  # 当这里用__name时,便会报错,没有name属性??这是什么意思??/
        Student.count += 1  # +=跟=+什么区别


# a = Student('lack')

# print(a.name)
# print(Student.count)
# b = Student('tom')
# print(Student.count)
# c = Student('naid')
# print(Student.count)

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


# 正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
# 使用slots
class Student(object):
    __slots__ = ('name', 'age')


a = Student()
a.name = 'jack'
a.age = 26

# a.score=90# 此时就会报错,因为上面进行了绑定


print()


# 3月11日

# @property 为了简化getter和setter方法?? 把方法改写成属性


# 关于@property @x.setter @x.deleter
# 1).只有@property表示只读。
# 2).同时有@property和@x.setter表示可读可写。
# 3).同时有@property和@x.setter和@x.deleter表示可读可写可删除。

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be interger!')
        if value < 0 or value > 100:
            raise ValueError('score must be in 0~100')
        self._score = value


# s = Student(100)  这样是不正确的,因为初始是没有参数的
s = Student()
s.score = 90
print(s.score)


# 如果只定义getter方法,不定义setter方法,则为只读属性

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value2):
        self._height = value2

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 10
s.height = 20
print(s.resolution)


# 多重继承,一个子类可以获得多个父类的的功能
# MixIn
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。
# 多种继承的查询继承顺序主要是根据拓扑排序的思想进行继承的





# 定制类__class__是啥意思
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 重写object中的方法
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__  # 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。


print(Student('Michal'))
s = Student('Jack')

print(list(range(1, 100))[5:10])

# 因为类的实例都是运行期创建出来的

print(callable(Student('tom')))


# 定制类

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):  # 将fib按下标那样取出来,x起到了什么作用,个人认为可能是起到了下标的作用
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


for n in Fib():
    print(n)

f = Fib()
print(f[0])
print(f[3])

print(range(3))

print()


class Student(object):
    def __init__(self):
        self.name = 'Michal'

    def __getattr__(self, attr):  # 设置动态返回属性
        if attr == 'score':
            return 90
        if attr == 'age':
            return lambda: 26
        raise AttributeError('No attribute')


s = Student()
print(s.name)
print(s.score)
print(s.age)  # 当默认属性中没有时,则默认返回none ,此时没有括号,则为函数的名字,返回的是函数的内存地址
print(s.age())  # 此时返回的是方法的结果


#  直接复制的程序,不是手敲的
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# __call__
class Student(object):
    def __init__(self):
        self.name = 'SY'

    def __call__(self, *args, **kwargs):  # call方法可以调用自身
        print('Hello,SY')


x = Student()
print(x.name)
x()

print()


# 3月12日

# 枚举
class Weekday(object):
    def __init__(self):
        self.name = 'Jack'

    Sun = 0
    Mon = 1
    Tue = 2


day1 = Weekday.Mon
print(day1)
name1 = Weekday().name  # 类中的属性(常量)可以直接用类名进行访问,但是self的属性需要创建实例才能进行访问,
print(name1)

from enum import Enum

# 下面定义了Month类型的枚举,可直接使用Month.Jan来引用一个常量
Month = Enum('A', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)  # 此时Month.Jan引用的常量为member
print(Month.Jan.name)  # member的名字是Jan
print(Month.Jan.value)  # member的value值为1

# 上面value值是自动赋给成员的int常量,默认从1开始计数,下面为枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '>=', member, ',', member.value)

# __members__属性的作用????


# 为了更精确的控制枚举类型,下面从Enum派生出自定义类
from enum import Enum, unique


@unique  # 用来检测没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Sun
print(Weekday.Sun.name)  # 输出变量的名字
print(Weekday.Sun.value)  # 输出变量的值

from enum import Enum, unique


class Gender(Enum):  # Enum可以把一组常量定义在一个class中,成员可以直接比较
    Male = 0
    Femal = 1


class Student(object):
    def __init__(self, name, gender):  # 之前由于把init写成int导致下面创建实例时出错
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

# 3月13日
#  ctrl+E 弹出当前文件



# 3月14日

import logging  # 此模块用来捕获错误信息,并把错误打印出来,然后程序还能继续执行完毕

try:
    print('try....')
    # r = 10 / 0
    r = 10 / 2
    print('result:', r)  # 由于上面错误这句将不会被执行
except ZeroDivisionError as e:
    logging.exception(e)
    print('except', e)
else:
    print('no error!')
finally:
    print('finally')
print('end')
# 当遇到错误时,程序会跳到执行except程序段,然后有finally直接执行finally后的,然后程序继续向下执行





from functools import reduce


def str2num(s):
    return int(s)  # 当下面的数中为7.6时,则会报错,invalid literal for int() with base 10: ' 7.6'
    # 意思为输出的为不可用的10进制整数


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    # return [ for x in ns]#  用这种怎么写代码
    return reduce(lambda a, x: a + x, ns)  # a+x是什么意思?


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 76')
    print('99 + 88 + 76 =', r)


main()

# 返回5的阶乘

n = 5
print(reduce(lambda x, y: x * y, range(1, 4)))  # ?为什么此处只有一个范围的时候可以用,range是表示哪个的范围


def foo(s):
    n = int(s)
    assert n != 0  # 如果此时断言失败,则会输出assertionError
    return 10 / n


def main():
    foo('0')


# main()



# logging
import logging

logging.basicConfig(level=logging.INFO)  # 定义logging的级别

s = '7'
n = int(s)
logging.info('n=%d' % n)  # 定义输出调试的信息
print(10 / n)
print('It is over.')

import unittest  # 编写单元测试用例必须导入unittest模块


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError
        if self.score >= 80:  # 这里的判断必须先判断>=80,因为判断是从上往下进行判断,如果先判断60则会出错,
            return 'A'
        if self.score >= 60:  # 此处用elif也可以,else
            return 'B'
        return 'C'


# 编写单元测试用例
# class TestStudent(unittest.TestCase):
#     def test_80_100(self):
#         s1 = Student('Jack', 90)
#         s2 = Student('Michal', 100)
#         self.assertEquals(s1.get_grade(), 'A')
#         self.assertEquals(s2.get_grade(), 'A')
#
#     def test_60_80(self):
#         s1 = Student('Jack', 65)
#         s2 = Student('Michal', 70)
#         self.assertEquals(s1.get_grade(), 'B')
#         self.assertEquals(s2.get_grade(), 'B')
#
#     def test_0_60(self):
#         s1 = Student('Jack', 50)
#         s2 = Student('Michal', 45)
#         self.assertEquals(s1.get_grade(), 'C')
#         self.assertEquals(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Jack', -1)
#         s2 = Student('Michal', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
#
# if __name__ == '__main__':
#     unittest.main()

# s1 = TestStudent()
# 上面的测试用例可以正常运行,但是测试用例下面的就输出不了,所以注释起来了

# 3月15日
f = open('/home/macbookpro/PycharmProjects/First/Function.py', 'r', encoding='UTF8')
# 上面默认为UTF8,但是如果要打开别的编码格式的文件,加上encoding='GBK'即可
s = f.readlines()  # 一次性读取所有内容并按行返回list
print(s)

a = f.read()  # 调用read()会一次性读取,并把所有文件内容加入内存,文件过大则会导致文件内存过大
print(a)

for line in f.readlines():
    print(line.strip())
    # 上面当有三个输出时,会调用3次f对象,则此时不会输出三次文件,当有一个close()时,则后面会报错
f.close()

with open('/home/macbookpro/PycharmProjects/First/Function.py', 'r') as f:
    print(f.read())

# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
# 上面errors为当出现不同编码格式的文件时所要进行的处理,最简单的为进行忽略,ignore




# 3月21日
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，
# 有的在os.path模块中。
import os

print(os.name)

print(os.uname())  # 系统的详细信息
print(os.environ)  # 操作系统中定义的环境变量
print(os.environ.get('PATH'))

print([x for x in os.listdir('.') if os.path.isdir(x)])  # os.path.isdir()用来判断是不是文件夹
# 上面为列出当前目录下的所有目录
print([x for x in os.listdir('.')])  # 列出当前路径下的文件名

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


# 上面是判断是py文件 os.path.splitext()可以直接让你得到文件的扩展名
# os.path.sqlit()函数可以把路径拆为两部分,后一部分总是最后级别的目录



# JSON



# 4月9日
# 计算BIM指数的函数
def bmi():
    name = input('Name:')
    height = input('Height(m):')
    weight = input('Weight(kg):')
    BIM = float(float(weight) / float(height) ** 2)
    print('您的BIM指数为:', BIM)
    if BIM < 18.5:
        print('您太轻了')
    elif BIM <= 25:
        print('标准体重哦')
    elif BIM > 25:
        print('您有点胖了哦')
    else:
        print('您太胖了,需要减肥了!!')


bmi()
for i in range(10):
    choose = input('您是否愿意继续计算BIM(y/n):')
    if choose == 'y':
        bmi()
    else:
        break
