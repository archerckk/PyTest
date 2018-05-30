from tkinter import *
import tkinter.messagebox as mess

'主界面设置'
root = Tk()
root.title('猜拳小游戏')

# root.geometry('300x300')

'窗口居中函数'
def center_pos(w, h):
    # 获取屏幕的宽高
    # ws = root.winfo_screenmmwidth()
    # hs = root.winfo_screenheight()

    ws,hs=root.maxsize()
    # 计算x，y位置
    x = (ws - w) / 2
    y = (hs - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_pos(300, 300)


class Player:
    def __init__(self):
        self.playername = StringVar()

        self.player = Toplevel(root)
        self.player.protocol('WM_DELETE_WINDOW', self.defend_close)
        self.player.title('角色创建')
        scnWidth, scnHeight = self.player.maxsize()
        tmppos = '%dx%d+%d+%d' % (300, 100, (scnWidth - 200) / 2, (scnHeight - 100) / 2)
        self.player.geometry(tmppos)

        Label(self.player, text='请输入你的角色名字：').grid(row=0, column=0, padx=10, pady=10)
        Entry(self.player, textvariable=self.playername).grid(row=0, column=1)

        Button(self.player, text='角色创建', command=self.check_name).grid(row=1, columnspan=2)

    '检查名字有效性函数'
    def check_name(self):
        if self.playername.get() == '':
            mess.showerror('提示', '请输入你的角色名字！！')
        elif not 4 <= len(self.playername.get()) <= 8:
            mess.showerror('提示', '你输入的角色名字长度不在【4-8个字符】内！！！')
        else:
            mess.showinfo('角色信息', '你创建的角色名为：【%s】' % self.playername.get())
            '通过destroy销毁窗口'
            self.player.destroy()
            player_create.config(state=DISABLED)

    def defend_close(self):
        mess.showinfo('提示', '关闭窗口采用默认名字【小强】')
        self.playername = '小强'
        self.player.destroy()
        player_create.config(state=DISABLED)


class Com:

    def __init__(self):
        self.com=Toplevel(root)
        self.com.protocol('WM_DELETE_WINDOW', self.defend_close)
        self.com.title('对手选择')
        scnWidth,scnHight=self.com.maxsize()
        tmppos='%dx%d+%d+%d'%(200,200,(scnWidth-200)/2,(scnHight-200)/2)
        self.com.geometry(tmppos)

        frame=LabelFrame(self.com,text='请选择你的对手：')
        frame.pack(fill=X,pady=20,anchor=CENTER)

        self.choices={1:'曹操',2:'刘备',3:'孙权'}
        self.var=IntVar()
        self.var.set(0)
        for num,name in self.choices.items():
            b=Radiobutton(frame,text=name,value=num,variable=self.var,indicatoron=False,command=self.compare).pack(fill=X)

    def compare(self):
        var=self.var.get()

        return var


    def defend_close(self):
        if self.var not in [1,2,3]:
            mess.showinfo('提示','请选择一个你的对手！！！')







    

'定义角色名变量'
player=Player
player_create=Button(root, text='角色创建', width=20, command=player)
player_create.place(relx=0.5, rely=0.3, anchor=CENTER)

com=Com
com_chose=Button(root, text='对手选择', width=20, command=com)
com_chose.place(relx=0.5, rely=0.6, anchor=CENTER)



mainloop()
