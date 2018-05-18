from tkinter import *

app=Tk()

def callback():
    print('你好')
menubar=Menu(app)
menubar.add_command(label='hello',command=callback)
menubar.add_command(label='quit',command=app.quit())

frame=Frame(app,width=500,height=500,background='white')
frame.pack()

'定义右键绑定事件方法'
def post(event):
    menubar.post(event.x_root,event.y_root)


frame.bind('<Button-3>',post)


mainloop()