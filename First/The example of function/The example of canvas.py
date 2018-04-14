# 4月10日

# 这是一个画布的例子
from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=4000, height=4000)  # 创建长宽4000的画布

# canvas.create_rectangle(100,100,300,300,fill="green")

# for i in range(0, 60):
#     canvas.move(1, 0, -3)
#     tk.update()
#     time.sleep(0.05)
Id1 = canvas.create_polygon(200, 0, 100, 100, 300, 100, fill="black")
canvas.pack()  # 将画布展示出来


def press_x(event):
    if event.keysym == "Up":
        canvas.move(1, 0, -3)
        canvas.itemconfigure(Id1, fill="green")

    elif event.keysym == "Down":
        canvas.move(1, 0, 3)
        canvas.itemconfigure(Id1, fill="red")
    elif event.keysym == "Left":
        canvas.move(1, -3, 0)
        canvas.itemconfigure(Id1, fill="yellow")

    else:
        canvas.move(1, 3, 0)
        canvas.itemconfigure(Id1, fill="blue")


canvas.bind_all("<KeyPress-Up>", press_x)
canvas.bind_all("<KeyPress-Down>", press_x)
canvas.bind_all("<KeyPress-Left>", press_x)
canvas.bind_all("<KeyPress-Right>", press_x)

# canvas.create_arc(10,10,200,80,start=0,extent=359,style=ARC)
tk.mainloop()
