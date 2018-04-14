import sys
import easygui as gui

if gui.ccbox(msg='请问还要继续嘛？',choices=['还是继续吧','还是算了吧']):
    gui.msgbox('已经折腾不动了')
else:
    sys.exit(0)
