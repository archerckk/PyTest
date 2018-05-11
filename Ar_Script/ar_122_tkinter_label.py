from tkinter import *

app=Tk()
img=PhotoImage(file='resources/icon.png')
test=Label(
    app,
   text='hello word',
   fg='green',
   font=("consolas",40),
    image=img,
    compound='right')

test.pack()

mainloop()


