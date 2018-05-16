from tkinter import *
import hashlib

app=Tk()

text=Text(app)
text.pack()

text.insert(1.0,'I trust fishc.com')
content=text.get(1.0,END)

'获取初次内容的hash摘要'
def getsig(content):
    m = hashlib.md5(content.encode())
    return m.digest()
digest=getsig(content)

'定义内容检查的方法'
def check():
    content = text.get(1.0, END)
    if getsig(content)!=digest:
        print('你所输入的内容已更改！')
    else:
        print('内容没有更改')
'新建一个检查按钮'
Button(app,text='检查',command=check).pack()
mainloop()