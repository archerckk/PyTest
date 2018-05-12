from tkinter import *


def test(content):
    return content.isdigit()


def calc():
    result = int(jia1.get()) + int(jia2.get())
    jia3.set(result)

app = Tk()
'声量字符串变量接收输入框的数值'
jia1=StringVar()
jia2=StringVar()
jia3=StringVar()
testReg = app.register(test)
'输入框1'
e_jiashu=Entry(app,textvariable=jia1,validate='key',
                    validatecommand=(testReg,'%P'))
e_jiashu.grid(row=0,column=0)
'+号'
jiahao=Label(app,text='+').grid(row=0,column=1)
'输入框2'
e_beijiashu = Entry(app, textvariable=jia2,validate='key',
                         validatecommand=(testReg, '%P'))
e_beijiashu.grid(row=0, column=2)
'=号'
dengyuhao = Label(app, text='=').grid(row=0, column=3)
'结果'
e_jieguo = Entry(app, textvariable=jia3,state='readonly')
e_jieguo.grid(row=0, column=4)

'计算按钮'
cal=Button(app,text='计算',command=calc)
cal.grid(row=1,column=2)





mainloop()