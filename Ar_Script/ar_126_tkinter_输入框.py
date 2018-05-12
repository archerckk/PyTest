from tkinter import *

app=Tk()


def show():
    print('作品:%s'%e_book.get())
    print('作者:%s' % e_name.get())

l_book=Label(app,text='作品:').grid(row=0,column=0,padx=10,pady=10)
l_name=Label(app,text='作者:').grid(row=1,column=0,padx=10,pady=10)
e_book=Entry(app)
e_name=Entry(app)
'有内容传输的要单独写grid或者pack'
e_name.grid(row=1,column=1,padx=10,pady=10)
e_book.grid(row=0,column=1,padx=10,pady=10)

b1=Button(app,text='作者信息',command=show).grid(row=2,column=0,sticky=W,padx=5,pady=5)
b2=Button(app,text='退出',command=app.quit()).grid(row=2,column=1,sticky=E,padx=5,pady=5)

mainloop()