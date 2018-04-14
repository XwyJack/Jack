# 计算BIM指数的函数

from tkinter import *
import tkinter.messagebox as messagebox


def BMI(high, weigh):
    check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    for i in list(high):
        if i not in check:
            return ('参数有错误,请输入数字')
    for i in list(weigh):
        if i not in check:
            return ('参数有错误,请输入数字')
    if not high or not weigh:
        return None

    BMI = float(weigh) / float(high) ** 2

    if BMI < 18.5:
        return '您的BMI指数为%.2f,您的身体装状况过轻.' % BMI
    elif BMI <= 25:
        return '您的BMI指数为%.2f,您的身体装状况正常.' % BMI
    elif BMI <= 28:
        return '您的BMI指数为%.2f,您的身体装状况过重.' % BMI
    elif BMI <= 32:
        return '您的BMI指数为%.2f,您的身体装状况肥胖.' % BMI
    else:
        return '警告%.2f' % BMI


class Application1(Frame):
    def __init__(self, master=None):  # 为什么加master跟不加maste没有区别 因为master只是控制此窗口是否为顶层窗口
        Frame.__init__(self, master)
        self.alertButton = Button(self, text='点击显示结果', command=self.result)
        self.nameinput2 = Entry(self)
        self.label2 = Label(self, text='请输入您的体重')
        self.nameinput1 = Entry(self)
        self.label1 = Label(self, text='请输入您的身高')
        # 以上这些之前都是放到creatWidgets中的,但是按照提示放到了__init__函数中,但不知道为什么
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1.pack()
        self.nameinput1.pack()

        self.label2.pack()
        self.nameinput2.pack()

        self.alertButton.pack()

    def result(self):
        BMI_result = BMI(self.nameinput1.get(), self.nameinput2.get()) or '请输入参数'
        messagebox.showinfo("BMI转换结果", '%s' % BMI_result)


app = Application1()
app.master.title('BMI转换器')
app.mainloop()
