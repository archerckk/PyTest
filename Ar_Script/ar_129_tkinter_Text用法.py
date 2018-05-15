from tkinter import *

app=Tk()


'设置tag属性'
text1=Text()
text1.tag_config('op1',background='blue',foreground='white')
text1.insert(INSERT,'Archer','op1')

'创建一个窗口对象在上面'
def show():
    print('我被点了一下')

b=Button(text1,command=show,text='点我点我')
b.grid()
'创建一个图片对象'
img=PhotoImage(file='resources/18.gif')

text1.window_create(INSERT,window=b)
text1.image_create(INSERT,image=img)
text1.pack()

mainloop()