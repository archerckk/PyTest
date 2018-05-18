from tkinter import *

app=Tk()
list1=[
    'one',
    'two',
    'three',
    'four'
]
var=StringVar()
'将默认值设置为列表的第一个选项'
var.set(list1[0])
'传入参数，位置，变量，解包列表参数'
w=OptionMenu(app,var,*list1)
w.pack()


mainloop()