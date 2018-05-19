from tkinter import *

app=Tk()

def show():
    top=Toplevel()
    top.attributes('-alpha',0.8)
    top.title('测试窗口')

    msg=Message(top,text='你看看我是不是弹出来了？',width=600)
    msg.pack()



Button(app,text='测试弹窗',command=show).pack()



mainloop()