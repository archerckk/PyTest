import easygui as gui

result=gui.buttonbox(msg='你喜欢哪一部动画：',images='timg.gif',choices=['海贼王','死神','火影','全职猎人'],title='动画选择')

print(result)