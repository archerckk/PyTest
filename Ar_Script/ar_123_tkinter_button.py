from tkinter import *


app=Tk()

frame1=Frame(app)
frame2=Frame(app)

var=StringVar()
var.set('您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！')


def callback():
    var.set('鬼才信你呢！！')

'定义文字标签'
textLabel=Label(
    frame1,
    textvariable=var
)
textLabel.pack(side=LEFT)

'定义图片标签'
img=PhotoImage(file='resources/18.gif')
photoLabel=Label(
    frame1,
    image=img
    # compound=RIGHT
)
photoLabel.pack(side=RIGHT)

'定义同意按钮'
agree=Button(
    frame2,
    text='已满18岁！',
    command=callback,
    # state=DISABLED

)
'按钮显示'
agree.pack()


frame1.pack(padx=10)
frame2.pack(padx=10,pady=10)
mainloop()
