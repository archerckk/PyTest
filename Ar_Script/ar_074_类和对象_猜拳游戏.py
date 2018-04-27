import random as r
import easygui as g

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
        msg = '请输入你要新建的角色名字：'
        title = '角色创建'
        toast = '你输入的角色名字多于8个字符'
        try:
            while 1:
                self.name = g.enterbox(msg, title)
                if len(self.name) > 8:
                    g.msgbox(toast, '提示')
                else:
                    break
        except TypeError:
            g.msgbox('取消输入默认采用名字【张三】')
            self.name='张三'
        self.win = 0
        self.lost = 0
        self.deuce = 0

    def getFinger(self):
        msg = '你要出的拳是：'
        title = '出拳选择'
        choices = ['剪刀', '石头', '布']
        self.finger = g.buttonbox(msg, title, choices)
        return self.finger


class Computer:
    def __init__(self):
        msg = '请选择你的对手：'
        titile = '对手选择'
        choices = ['刘备', '孙权', '曹操']
        self.name = g.buttonbox(msg, titile, choices)
        self.win = 0
        self.lost = 0
        self.deuce = 0

    def getFinger(self):
        choices = ['剪刀', '石头', '布']
        self.finger = r.choice(choices)
        g.msgbox('【%s】出【%s】' % (self.name,self.finger), '提示')
        return self.finger


class Game:
    def __init__(self, player, com):

        self.player = player
        self.com = com

    def judge(self):
        if (self.player.finger == '剪刀' and self.com.finger == '布') or (
                        self.player.finger == '石头' and self.com.finger == '剪刀') or (
                        self.player.finger == '布' and self.com.finger == '石头'):

            self.player.win += 1
            self.com.lost += 1
            g.msgbox('恭喜【%s】，取得胜利'%self.player.name)
        elif (self.player.finger == '石头' and self.com.finger == '布') or (
                        self.player.finger == '布' and self.com.finger == '剪刀') or (
                        self.player.finger == '剪刀' and self.com.finger == '石头'):

            self.player.lost += 1
            self.com.win += 1
            g.msgbox('愚蠢的【%s】，你输了'%self.player.name)
        else:
            self.player.deuce += 1
            self.com.deuce += 1
            g.msgbox('平分秋色，不分胜败！')

    def gameStart(self):
        count=5

        while 1:

            self.player.getFinger()
            self.com.getFinger()
            self.judge()
            count -= 1

            if count == 0:
                msg = '是否继续游戏？'
                title = '提示'
                decide = g.ccbox(msg, title, choices=['是', '否'])
                if decide:
                    count = 5
                    continue
                else:
                    msg = '【%s】的战绩如下：' % self.player.name
                    title = '对战结果'
                    content = '胜：%d场\t\t负：%d场 \t\t平：%d场\n' % (self.player.win, self.player.lost, self.player.deuce)
                    g.textbox(msg, title, content)
                    break

# def testmethod():
#     print('test')


# player = Player()
#
# com = Computer()
#
# game = Game(player, com)
# game.start()
