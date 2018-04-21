import easygui as g

class NameFormat:

    def __init__(self):
        self.name1_list = ['皮球','小皮球','笨皮球','小学森','小皮蛋','调皮蛋','梅清','吕梅清','乖宝宝','旺夫','笨笨猪'
                           ,'笨猪','小宝宝','宝宝猪']
        self.name2_list=['外星人','老公','智斌','陈智斌','旺妻','臭臭','乖臭臭','臭猪','臭臭猪']
        self.name1=''
        self.name2=''
        self.judge=1

    def game_start(self):
        name1_msg='请输入你的名字：'
        name2_msg='请输入你感兴趣的人的人的名字：'
        name_title='知你所想'
        while 1:

            while 1:
                self.name1 = g.enterbox(name1_msg, name_title, default='')
                try:
                    if self.name1 not in self.name1_list:

                        g.msgbox('你怎么会连自己叫什么都不知道呢？')
                        continue
                    else:
                        g.msgbox('恭喜！！你知道自己是%s啦！'%self.name1)
                        break
                except KeyboardInterrupt:
                    g.msgbox('不输入正确，是不能取消的！！')
                    continue

            while 1:
                self.name2 = g.enterbox(name2_msg, name_title, default='')
                if self.name2 not in self.name2_list:
                    g.msgbox('害羞啥？你还是面对自己的真实想法吧！！')
                    continue
                else:
                    g.msgbox('%s爱%s一生一世！！我们会一直好好的……'%(self.name1,self.name2))
                    break
            self.judge=g.ccbox('是否继续游戏？','知你所想',choices=['是','否'])
            if self.judge:
                continue
            else:
                g.msgbox('游戏结束')
                break

nameFormat=NameFormat()
# nameFormat.game_start()