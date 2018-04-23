import easygui as g
'''
提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容
'''

filePath=g.fileopenbox('选择你要打开的文件','文件','*')

with open(filePath)as f:
    content=f.read()

g.textbox('文件内容显示如下：','标题',content)