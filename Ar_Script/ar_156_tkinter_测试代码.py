from tkinter import *

app=Tk()

def show():
    f=LabelFrame(app,width=100,height=100)
    f.place(relx=0.5,rely=0.5,anchor=CENTER)
    Label(f,text='测试').grid(row=0,column=0)
    Entry(f).grid(row=0,column=1)



Button(app,text='点我',command=show).place(relx=0.5,rely=0.5,anchor=CENTER)

mainloop()