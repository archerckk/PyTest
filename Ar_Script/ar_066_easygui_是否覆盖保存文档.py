import easygui as g
import os

'''当用户点击【OK】按钮时候，比较当前文件是否修改过，如果修改过，则提示【覆盖保存】、【放弃保存】、【另存为】'''

'''
1.打开一个文件，并且显示文本的内容
2.点击文本框的【OK】按钮弹出一个选择选择框（如题要求）
3.选择框功能
    【覆盖保存】写入内容保存在原来的目录
    【放弃保存】直接终止操作
    【另存为】打开另外一个文件选择框，写入更改内容，保存文件
'''

filePath=g.fileopenbox('请选择你的文件','文件',"*txt")
title=os.path.basename(filePath)
msg='文件【%s】的内容显示如下：'%title
with open(filePath)as f:
    content=f.read()
    content=g.textbox(msg,title,content)

differ=[]

with open(filePath)as f:
    old=f.read()
    # for i in content:
    #     if i!=f.readline():
    #         differ.append(i)

# if len(differ)!=0:
if old!=content[:-1]:
    msg='检测文件内容发生改变，请选择以下操作'
    title='警告'
    choices=['覆盖保存','放弃保存','另存为']
    result=g.indexbox(msg,title,choices)

    if result==0:
        with open(filePath,'w')as f:
            f.writelines(content)
    elif result==1:
        pass
    elif result==2:
        otherPath=g.filesavebox('请选择你的文件','文件','*.txt',)
        with open(otherPath,'w')as f:
            f.writelines(content)
else:
    pass


