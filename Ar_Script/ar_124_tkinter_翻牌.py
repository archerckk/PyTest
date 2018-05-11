from tkinter import *

app=Tk()

girls=['蒂法','女帝','Saber','亚丝娜']
v=[]

for girl in girls:
    v.append(IntVar())
    b=Checkbutton(app,text=girl,variable=v)
    b.pack(anchor=W)
for girl in girls:
    toast=Label(app,textvariable=v).pack()
mainloop()