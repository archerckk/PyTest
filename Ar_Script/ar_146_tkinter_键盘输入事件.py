from tkinter import *

app=Tk()
frame=Frame(app,width=300,height=300,background='black')

def callback(event):
    print('刚才按键为：',event.keysym)

frame.bind('<Key>',callback)
'主要要有焦点获取'
frame.focus_set()

frame.pack()
mainloop()