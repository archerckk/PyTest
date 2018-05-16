from tkinter import *

app=Tk()
text=Text(app,undo=True,autoseparator=False)
text.pack()

text.insert(1.0,'I trust fishc.com')

'待注释'
def callback(event):
    text.edit_separator()
text.bind('<Key>',callback)

'定义撤销方法，添加撤销按钮'
def show():
    text.edit_undo()

Button(app,text='撤销',command=show).pack()



mainloop()