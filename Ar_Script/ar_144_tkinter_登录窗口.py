from tkinter import *

root=Tk()
'定义账号标签和账号输入框'
Label(root,text='账号:').grid(column=0,sticky=W)
account_entry=Entry(root)
account_entry.grid(row=0,column=1)

'定义面膜标签和密码输入框'
Label(root,text='密码:').grid(row=1,column=0,sticky=W)
psw_entry=Entry(root,show='*')
psw_entry.grid(row=1,column=1)

'右边logo定义,要跨行的话是要定义在第几行的'
img=PhotoImage(file='resources/18.gif')
Label(root,image=img).grid(row=0,rowspan=2,column=2,padx=5,pady=5)

'登录函数，登录按钮'
def show():
    print('Hello')
Button(root,command=show,text='登录',width=20).grid(row=2,columnspan=3,pady=5)

mainloop()