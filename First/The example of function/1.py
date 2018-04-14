print("Hello World!")



#注释
a=5
b=6
c=a+b
print(c)


#非波那且数列
a,b=0,1
while b<10:
    print(b,end='')#end用来表示不进行换行回车，end关键字
    a,b=b,a+b

print()
x=input("please input x:")
input("Please Enter")#可以让程序停一下，Enter的作用？

#1字符串和数值直接输出
print(1)#输出字符型
print("character")#字符串
#2变量输出
x=12
print(x)

#3格式化输出
s="Hello"
x=len(s)
print("The length of %s is %d"%(s,x))


#IF条件控制语句
var1=1
if var1:
    print("1-if的条件控制为true")
    print(var1)
var2=0
if var2:#因为var2为0（假）,所以后面不会执行
    print("1-if的条件控制为true")
    print(var2)
print("goodbye!")


