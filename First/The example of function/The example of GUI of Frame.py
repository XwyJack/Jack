from  tkinter import *  # 第一步


class Application(Frame):  # 第二步
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world! My first window')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


app = Application()  # 第三步
# 设置窗口标题:
app.master.title('Hello World,My first window')  # 设置标题,应该是内置
# 主消息循环:
app.mainloop()



# 4月9日
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.nameInput = Entry(self)
        print('类创建时已经使用')  # 此处表明类创建时已经使用了此初始化构造函数
        self.pack()
        self.creatWidgets()

    def creatWidgets(self):
        self.nameInput.pack()
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World!'
        messagebox.showinfo('Message', 'Hello,%s' % name)


app = Application()
app.master.title('Hello ,World!')
app.mainloop()
