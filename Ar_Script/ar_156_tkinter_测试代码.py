from tkinter import *
# import tkinter as tk

app=Tk()

# def show():
#     f=LabelFrame(app,width=100,height=100)
#     f.place(relx=0.5,rely=0.5,anchor=CENTER)
#     Label(f,text='测试').grid(row=0,column=0)
#     Entry(f).grid(row=0,column=1)
#
#
#
# tk.Button(app,text='点我',command=show).place(relx=0.5,rely=0.5,anchor=CENTER)
class A:
    def __init__(self):
        self.v=StringVar()



    def a(self):
        Entry(app,textvariable=self.v).pack()
        Button(app,command=self.b).pack()
        print('这是方法a')
        print(self.v.get())

    def b(self):
        print('这是方法b')
        print(self.v.get())
        self.c()

    def c(self):
        print('这是方法c')
        print(self.v.get())


x=A()
x.a()
x.b()


mainloop()