from tkinter import *

app=Tk()
def callback():
    print('你好')
mb=Menubutton(app,text='点我点我',relief=RAISED)
mb.pack()

filemenu=Menu(mb)
filemenu.add_command(label='新建',command=callback)
filemenu.add_command(label='打开',command=callback)
filemenu.add_command(label='保存',command=callback)
filemenu.add_separator()
filemenu.add_command(label='退出',command=app.quit())

mb.config(menu=filemenu)



mainloop()