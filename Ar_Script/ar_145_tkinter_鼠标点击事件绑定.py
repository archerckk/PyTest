from tkinter import *

app=Tk()
frame=Frame(app,width=300,height=300,background='black')
frame.pack()

def callback(event):
    print('刚才点击位置的坐标为：',(event.x,event.y))

frame.bind('<Button-1>',callback)


mainloop()