import easygui as g
import sys

while 1:
    g.msgbox('这是第一个图形小游戏！')

    '定义选项窗口的提示，标题还有选项'
    msg='请问你有什么兴趣？'
    title='兴趣咨询'
    choices=['羽毛球','睡觉','玩游戏','看书']
    choice=g.choicebox(msg,title,choices)

    g.msgbox('你的兴趣是:'+choice,'结果')

    '定义确认弹框的内容和标题'
    msg='你要继续游戏嘛？'
    title='提示'
    choices=['是','否']
    decide=g.ccbox(msg,title,choices)

    if decide:
        pass
    else:
        sys.exit()