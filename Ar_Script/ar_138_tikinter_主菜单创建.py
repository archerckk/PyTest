from tkinter import *

app=Tk()

def callback():
    print('你好')
menubar=Menu(app)
menubar.add_command(label='hello',command=callback)
menubar.add_command(label='quit',command=app.quit())


app.config(menu=menubar)


mainloop()