from tkinter import *
app=Tk()
def callback():
    print('你好')
menubar=Menu(app)

'创建文件菜单'
newvar=IntVar()
openvar=IntVar()
savevar=IntVar()


filemenu=Menu(menubar,tearoff=False)
filemenu.add_checkbutton(label='新建',command=callback,variable=newvar)
filemenu.add_checkbutton(label='打开',command=callback,variable=openvar)
filemenu.add_checkbutton(label='保存',command=callback,variable=savevar)
filemenu.add_separator()
filemenu.add_command(label='退出',command=app.quit())
'添加父级菜单'
menubar.add_cascade(label='文件',menu=filemenu)


'创建文件菜单'
choicevar=IntVar()
editmenu=Menu(menubar,tearoff=False)
editmenu.add_radiobutton(label='撤销',command=callback,variable=choicevar,value=1)
editmenu.add_radiobutton(label='复制',command=callback,variable=choicevar,value=2)
editmenu.add_radiobutton(label='剪切',command=callback,variable=choicevar,value=3)
editmenu.add_separator()
editmenu.add_command(label='粘贴',command=callback)
'添加父级菜单'
menubar.add_cascade(label='编辑',menu=editmenu)


app.config(menu=menubar)
mainloop()