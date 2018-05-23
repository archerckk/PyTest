from tkinter import *
import random as r
import tkinter.messagebox as mess
'''
1.玩家类
    新建玩家的名字
        限制输入内容，输入长度
    玩家自主选择出拳
        限制输入内容(剪刀石头布选项)
2.电脑类
    选择对战的电脑
    电脑出拳（随机）  
3.游戏类
    初始化玩家和电脑
    判断方法
        台词的设计
    胜负统计
        连胜连负的消息处理
'''

app=Tk()

'设置窗口标题'
app.title('猜拳小游戏')

'设置游戏窗口大小'
app.geometry('300x300')



class Player:

    def __init__(self):
        pass


    def create(self):
        '设置弹出窗口的属性'
        self.player = Toplevel(app)
        self.player.title('角色创建')
        self.player.geometry('350x100')
        self.player.protocol('WM_DELETE_WINDOW',self.defend_close)

        self.var = StringVar()
        self.lb = Label(self.player, text='请输入你的角色名字：', )
        self.lb.grid(column=0, padx=5, pady=5)
        self.name = Entry(self.player, textvariable=self.var)
        self.name.grid(row=0, column=1)

        self.create_button = Button(self.player, text='角色创建', width=20,command=self.check)
        self.create_button.grid(row=2, columnspan=3,pady=10)

        return self.name

    def check(self):

        if self.name.get()=='':
            mess.showerror('提示','请输入你的角色名字！！')
        elif not 4<=len(self.name.get())<=8:
            mess.showerror('提示','你输入的角色名字长度不在【4-8个字符】内！！！')
        else:
            mess.showinfo('角色信息','你创建的角色名为：【%s】'%self.name.get())
            '通过destroy销毁窗口'
            self.player.destroy()


    def defend_close(self):
        mess.showwarning('警告','还没输入用户名，还能关闭！！')


    def guess(self):

        lf=LabelFrame(self.player,text='你要选择出的拳是：')
        lf.grid(row=1,column=1)

        fingers=[('剪刀',1),('石头',2),('布',3)]
        v=IntVar()
        for name,value in fingers:
            Radiobutton(lf,text=name,value=value,variable=v).grid(row=2,column=2)

player=Player()


name=Button(app,text='角色创建',width=20,command=player.create).place(relx=0.5,rely=0.3,anchor=CENTER)



mainloop()














# player.guess()