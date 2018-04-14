# 用while计算1-100的和
n = 100
sun = 0
counter = 1

while counter <= n:
    sun = sun + counter
    counter += 1
print("1到%d的和为:%d" % (n, sun))

# 利用把判断条件设置为永远为真，来实现无限循环
# var = 1
# while var == 1:
#     try:  # try except 用来调整异常，当害怕输入的数字有错误时使用
#         num = int(input("输入一个数字："))
#         print("输入的数字是：", num)
#     except ValueError:
#         print("您输入的数字有错")
# print("Goodbye!")

# while跟else一块使用
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于5")

# 无限循环输出
# flag = 1
# while flag : print("欢迎")
# print("Goodbye!")




# for循环
languages = ["C", "C++", "Java", "Python"]
for i in languages:
    if i == "Java":
        print("菜鸟教程")
        break  # 跳出当前循环体，也就是跳出for的循环，直接到最后
    # print("循环数据",i)#跟下面的语句是同样的效果，只要print与if同缩进
    else:
        print("循环数据", i)
else:
    print("没有循环数据")
print("完成循环")

# range函数
for i in range(5):
    print(i)

for x in range(5, 9):
    print(x)
for y in range(0, 10, 3):
    print(y)

# 用range跟len函数创建一个序列的索引
a = ["taobao", "tecent", "sina", "baidu"]
for i in range(len(a)):
    print(i + 1, a[i])  # i+1决定i的标号从1开始

# 使用range函数来创建一个列表
print(list(range(5)))

# break语句
for letter in "Rounber":
    if letter == 'b':
        break
    print("当前的字母为：", letter)

var = 10
while var > 0:
    print("var的值为：", var)
    var -= 1  # var=var-1
    if var == 5:
        continue  # continue为跳出当前循环，然后进入下次循环
        # break
print("Goodbye!")

# 查询质数，循环中用else语句
for x in range(2, 10):
    for y in range(2, x):
        if x % y == 0:
            print(x, "等于", y, '*', x // y)
            break
    else:
        # 循环中没有找到元素
        print(x, '是质数')


# 最小的类
class MyEmptyClass:
    print("最小的类")
    pass  # 站位语句，不执行任何操作


for letter in 'runoob':
    if letter == 'o':
        pass
        print("执行pass语句")
    else:
        print("当前字母：", letter)
print("Goodbye!")

# for循环计算1-100的和
n = 0
sun = 0
for n in range(0, 101):
    sun += n
print(sun)

# 9*9 乘法表
i = 1  # i是行数，外层循环，控制多少行
while i <= 9:
    j = 1  # 里面一层为外层循环，控制列数，内层循环一般一定会包含外层循环的变量
    while j <= i:
        mut = i * j
        print("%d*%d=%d" % (j, i, mut), end=" ")
        j += 1
    print("")
    i += 1

# 输出阶梯形状的×
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end='')
    else:
        print('\r')

# 用sum求和,因为前面用到了sum变量，所以此处的sum方法可能被认为为变量，所以上面的sum变量要变为sun
f = int(sum(range(101)))
print(f)

# 利用continue输出奇数
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# 利用循环条件输出奇数
print("")
b = 1
while b < 10:
    if b % 2 == 1:
        print(b)
    b += 1  # 执行玩此语句后会执行while后面的判断
print("输出结束")

# 利用字典来查询成绩,初始化时指定数据
d = {"a": 90, "b": 98, "c": 95}
print(d["a"])

# 利用key指定数据
g = {}# 正常不会这么用,像上面那样用,大括号{}用来创建空的字典
g['Jack'] = 97
print(g['Jack'])

# 使用in方法查看key是否存在
print('Jack' in g)

# set表示一组key值的集合,可以使用{}和set()函数来创建如下,
s = set([1, 2, 3, 4])
# s={1,2,3,4}
print(s)
s.remove(3)  # remove可以删除元素
print(s)

s1 = set([1, 2, 3, 4])
s2 = set([2, 3, 4, 5])
print(s1 & s2)  # set可以做数学意义上的交集,并集
print(s1 | s2)




