import easygui as gui
import sys

def msgbox(msg='这是默认展示的消息!!',ok_button='加油！',title='激励自己'):
    gui.msgbox(msg=msg,ok_button=ok_button,title=title)


msgbox()