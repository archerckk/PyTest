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


class Player:

    def __init__(self):
        self.player=Tk()
        # self.player.overrideredirect(True)


        self.name=StringVar()
        Label(self.player,text='请输入你的角色名字：',).grid(column=0,padx=5,pady=5)
        self.name=Entry(self.player,textvariable=self.name)
        self.name.grid(row=0,column=1)
        Button(self.player,text='角色创建',command=self.create).grid(row=1,columnspan=2)
        mainloop()

    def create(self):
        if self.name.get()=='':
            mess.showerror('提示','请输入你的角色名字！！')
        elif not 4<=len(self.name.get())<=8:
            mess.showerror('提示','你输入的角色名字长度不在【4-8个字符】内！！！')
        else:
            mess.showinfo('角色信息','你创建的角色名为：【%s】'%self.name.get())
            self.player.quit()

    def guess(self):

        lf=LabelFrame(self.player,text='你要选择出的拳是：')
        lf.grid()
        fingers=[('剪刀',1),('石头',2),('布',3)]
        v=IntVar()
        for name,value in fingers:
            Radiobutton(lf,text=name,value=value,variable=v).grid(row=0,column=0)



player=Player()
player.guess()