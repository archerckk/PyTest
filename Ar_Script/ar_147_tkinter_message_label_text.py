from tkinter import *
app=Tk()
def show_label():
    '在宽度不够的时候会显示不全'
    Label(app,text='这是一条超级超级超级超级超级超级长的信息',width=10).pack()

def show_text():
    t1=Text(app,width=10)
    t1.insert(INSERT,'这是一条超级超级超级超级超级超级长的信息')
    t1.pack()

def show_message():
    Message(app, text='这是一条超级超级超级超级超级超级长的信息', width=10).pack()

b1=Button(app,text='Label',command=show_label)
b1.pack()
b2=Button(app,text='text',command=show_text)
b2.pack()
b3=Button(app,text='message',command=show_message)
b3.pack()


mainloop()