import easygui as gui
import sys

while 1:
    gui.msgbox('嗨，欢迎进入第一个界面小游戏^_^')

    msg='请问你希望在鱼c工作室学习到什么知识？'
    title='小游戏互动'
    choices=['谈恋爱','编程','OOXX','打飞机']

    choice=gui.choicebox(msg,title,choices)

    gui.msgbox('你的选择是：'+choice,title='结果')
    msg='你希望重新开始小游戏吗？'
    title='请选择'

    if gui.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
