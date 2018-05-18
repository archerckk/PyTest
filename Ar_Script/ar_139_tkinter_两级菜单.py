from tkinter import *
app=Tk()
def callback():
    print('你好')
menubar=Menu(app)

'创建文件菜单'
filemenu=Menu(menubar,tearoff=False)
filemenu.add_command(label='新建',command=callback)
filemenu.add_command(label='打开',command=callback)
filemenu.add_command(label='保存',command=callback)
filemenu.add_separator()
filemenu.add_command(label='退出',command=app.quit())
'添加父级菜单'
menubar.add_cascade(label='文件',menu=filemenu)


'创建文件菜单'
editmenu=Menu(menubar,tearoff=False)
editmenu.add_command(label='撤销',command=callback)
editmenu.add_command(label='复制',command=callback)
editmenu.add_command(label='剪切',command=callback)
editmenu.add_separator()
editmenu.add_command(label='粘贴',command=callback)
'添加父级菜单'
menubar.add_cascade(label='编辑',menu=editmenu)




app.config(menu=menubar)
mainloop()