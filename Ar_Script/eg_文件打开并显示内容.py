import easygui as g
import os

file=g.fileopenbox(title='文件选择',msg='请选择你要打开的文件',default='./*.txt',filetypes=['.txt','txt文档'])
file_name=os.path.basename(file)
with open(file)as txt_file:
    content=txt_file.read()
g.textbox(title='显示文件内容',msg='文件【%s】的内容显示如下'%file_name,text=content)


