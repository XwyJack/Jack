# 4月10日

# 一个简单的框
import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text='Hello World!')
label.pack()
button = tkinter.Button(root, text='quit', command=quit)  # 之前写成了quit()怎么都调试不出来界面,然后把括号去掉,则成功了
button.pack(side='left')  # side来决定在窗体的什么地方

root.mainloop()

# 第二个label的例子
# 将label添加至主窗口的上中下
from tkinter import *


def introduce():  # 此处定义的函数为了让下面的button中的command的参数
    print('Hello')


root = Tk()
root.geometry('500x500')  # 设置主窗体的大小

# 创建三个 Label 分别添加到root窗体中
# Label是一种用来显示文字或者图片的组件
Label(root, text='pack1', bg='red', fg='white', width=5, height=5, anchor='sw').pack()
Label(root, text='pack2', bg='blue').pack()
Label(root, text='pack3', bg='green').pack()

Entry(bg='black', fg='white', show='*').pack()  # 新增加的输入框
Button(root, text='quit', bg='black', fg='red', command=introduce).pack(side='bottom')  # 新增加的按钮
# 上面command中的参数为上面定义的函数introduce
root.mainloop()

# 两个list列表的显示
from tkinter import *

root = Tk()  # 创建主窗口

li = ['Python', 'Java', 'C', 'PHP']  # 创建两个列表
qianduan = ['Css', 'Jqurey', 'JS', 'BOotstrap']
# 创建两个控件
lisb = Listbox(root)
lisb2 = Listbox(root)
# 第一个控件插入数据
for item in li:
    lisb.insert(0, item)
# 第二个控件插入数据
for item in qianduan:
    lisb2.insert(0, item)
# 将小部件插入窗口
lisb.pack()
lisb2.pack()
# 消息进入主循环
root.mainloop()
