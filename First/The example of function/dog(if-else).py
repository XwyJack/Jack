import random  # alt+2次enter会出现自动修改的信息

age = int(input("请输入你家狗狗的年龄："))
print("")
if age < 0:
    print("你他妈在逗我吧")
elif age == 1:
    print("相当与10岁的人")
elif age == 2:
    print("相当与20岁的人")
else:
    print("滚")
input("点击enter推出")

# ==等于，比较对象是否相等

print(5 == 6)
x = 5
y = 6
print(x == y)

# 猜迷游戏
guess = -1
number = 7
print("数字猜迷游戏")
while guess != number:  # 第一个控制 所以当两个参数相等后退出程序，这是while所决定的
    guess = int(input("请输入你的数字："))

    if guess == number:
        print("恭喜你才对了！")
    elif guess > number:
        print("你猜的大了")
    elif guess < number:
        print("你猜的小了")

# if嵌套语法
num = int(input("请输入你的数字："))
if num % 2 == 0:
    if num % 3 == 0:  # 套了一个if
        print("数字既能被2整除，也能被3整除")
    else:
        print("只能被2整除，不能被3整除")
else:
    if num % 3 == 0:  # else中又套了一个if
        print("只能被3整除")
    else:
        print("数字既不能整除2,也不能整除3")

# break
for letter in 'python':
    if letter == 'h':
        break
    print('current letter:', letter)

var = 10
while var > 0:  # 缩进用来控制结构
    print("current variable:", var)
    var -= 1  # var = var - 1相同的作用
    if var == 5:
        break
print("Good Bye!")

x = random.choice(range(1, 100))
print("x=", x)
y = random.choice(range(1, 100))
print("y=", y)
if x > y:
    print("x:", x)
elif x == y:
    print("x+y", x + y)
else:
    print("y:", y)

# 狗狗年龄对比加强版

print("---输入你家狗狗的年龄---")
while True:
    try:
        age = int(input("输入你家狗狗的年龄"))
        if age < 0:
            print("你在逗我吗")
        elif age == 1:
            print("相当与14岁的人")
            break
        elif age == 2:
            print("相当与22岁的人")
            break
        else:
            human = 22 + (age - 2) * 5
            print("相当与人类", human)
            break
    except ValueError:
        print("输入不合法，请重新输入")

input("点击Enter退出")  # 因为我们都知道input是以换行作为输入结束的标志的,所以按enter后便退出程序结束了
