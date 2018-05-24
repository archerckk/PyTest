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

# app=Tk()
#
# '设置窗口标题'
# app.title('猜拳小游戏')
#
# '设置游戏窗口大小'
# app.geometry('300x300')


class Player(Toplevel):

    def __init__(self):
        super().__init__()
        '设置弹出窗口的属性'
        self.title='角色创建'
        self.geometry='350x100'
        self.var = StringVar()
        self.create()

    def create(self):
        self.protocol('WM_DELETE_WINDOW',self.defend_close)


        Label(text='请输入你的角色名字：').grid(column=0, padx=5, pady=5)

        Entry(textvariable=self.var).grid(row=0, column=1)

        self.create_button = Button(text='角色创建', width=20,command=self.check)
        self.create_button.grid(row=2, columnspan=3,pady=10)

        # main.name.config(state=DISABLED)

        return self.var

    def check(self):

        if self.var.get()=='':
            mess.showerror('提示','请输入你的角色名字！！')
        elif not 4<=len(self.var.get())<=8:
            mess.showerror('提示','你输入的角色名字长度不在【4-8个字符】内！！！')
        else:
            mess.showinfo('角色信息','你创建的角色名为：【%s】'%self.var.get())
            '通过destroy销毁窗口'
            self.destroy()


    def defend_close(self):
        mess.showinfo('提示','关闭窗口采用默认名字【小强】')
        self.var='小强'
        self.destroy()


    def guess(self):

        LabelFrame(text='你要选择出的拳是：').grid(row=1,column=1)

        fingers=[('剪刀',1),('石头',2),('布',3)]
        v=IntVar()
        for name,value in fingers:
            Radiobutton(text=name,value=value,variable=v).grid(row=2,column=2)


class Main_ui(Tk):
    def __init__(self):
        super().__init__()
        self.title='猜拳小游戏'
        self.geometry='300x300'

        self.name=Button(text='角色创建', width=20, command=self.create)
        self.name.place(relx=0.5, rely=0.3, anchor=CENTER)

    def ui_set(self):
        pass

    def create(self):
       player=Player()
        # pass




if __name__=='__main__':

    main=Main_ui()

    # player = Player()
    # mainloop()
    main.mainloop()
















# player.guess()