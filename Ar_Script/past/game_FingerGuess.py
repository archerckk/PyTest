import random as r
import easygui as g

'''
1.玩家类
    新建玩家的名字
        限制输入内容，输入长度
    玩家自主选择出拳
        限制输入内容，
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
        msg = '请输入你的名字：'
        title = '角色创建'

        while 1:
            self.name = g.enterbox(msg, title)
            try:
                length_name = len(self.name)
            except TypeError:
                self.name='玩家'
                g.msgbox('你取消了名字输入，采用默认名字：【%s】'%self.name)
                break
            if length_name > 8:
                g.msgbox('你输入的角色名大于8个字符！！！')
                continue
            elif length_name == 0:
                g.msgbox('请输入你的名字！！！')
                continue
            else:
                break
        self.choice = 0

    def guess(self):
        msg_choice = '你要出的是：'
        title = '猜拳'
        choices = ['剪刀', '石头', '布']
        self.choice = g.buttonbox(msg_choice, title, choices)
        if self.choice !=None:
            msg_toast = '【%s】出的是【%s】' % (self.name, self.choice)
            g.msgbox(msg_toast, title)
        return self.choice


class Computer:
    # 初始化电脑的角色选择
    def __init__(self):
        msg = '请选择你要对战的角色'
        title = '对战角色选择'
        choices = ['曹操', '刘备', '孙权']
        self.name = g.buttonbox(msg, title, choices)
        if self.name==None:
            self.name='曹操'
            g.msgbox('取消选择，默认选择【曹操】')
        self.guess = '布'

    # 电脑随机出拳方法
    def random_guess(self):
        self.guess = r.choice(['剪刀', '石头', '布'])
        # self.guess = r.choice(['布'])
        title = '猜拳'
        msg = '【%s】出的是【%s】' % (self.name, self.guess)
        g.msgbox(msg, title)
        return self.guess


class Game:
    def __init__(self):
        self.con = True
        self.win = 0
        self.lose = 0
        self.draw = 0

    def judge(self, Player, Computer):
        judge = True
        while judge:
            player_guess = Player.guess()
            if player_guess==None:
                g.msgbox('游戏中断')
                break
            computer_guess = Computer.random_guess()
            if computer_guess == None:
                g.msgbox('游戏中断')
                break
            if (player_guess == '剪刀' and computer_guess == '布') or (
                            player_guess == '石头' and computer_guess == '剪刀') or (
                            player_guess == '布' and computer_guess == '石头'):
                g.msgbox('你击败了【%s】，胜局数+1' % Computer.name)
                self.win += 1
            elif (player_guess == '剪刀' and computer_guess == '石头') or (
                            player_guess == '石头' and computer_guess == '布') or (
                            player_guess == '布' and computer_guess == '剪刀'):
                g.msgbox('你输了，负局数+1')
                self.lose += 1
            # elif (player_guess == '剪刀' and computer_guess == '剪刀') or (
            #                 player_guess == '石头' and computer_guess == '石头') or (
            #                 player_guess == '布' and computer_guess == '布'):
            else:
                g.msgbox('平局，平局数+1')
                self.draw += 1
            judge = g.ccbox('你是否继续游戏？', '提示', ['继续', '结束'])
            # if judge:
            #     continue
            # else:
            #     break
        g.msgbox('你的最终战绩为：胜：%d\t负：%d\t平：%d' % (self.win, self.lose, self.draw))
        g.msgbox('游戏结束')


# player = Player()
# computer = Computer()
# game = Game()
# game.judge(player, computer)
