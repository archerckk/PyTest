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

try:
    title=os.path.basename(filePath)

    msg='文件【%s】的内容显示如下：'%title

    '拿到新老两个文本内容'
    with open(filePath)as f:
        content=f.read()
        content_new=g.textbox(msg,title,content)

    '图像处理的text会默认在后面多添加一个换行符，所以不取最后一个字符，判断他们是否一样'
    if content!=content_new[:-1]:
        msg='检测文件内容发生改变，请选择以下操作'
        title='警告'
        choices=['覆盖保存','放弃保存','另存为']
        result=g.indexbox(msg,title,choices)

        if result==0:
            with open(filePath,'w')as f:
                f.writelines(content_new)
        elif result==1:
            pass
        elif result==2:
            otherPath=g.filesavebox('请选择你的文件','文件','*.txt',)

            '假如输入名字没有.txt后缀，补全扩展名'
            ext=os.path.splitext(otherPath)[1]
            if ext!='.txt':
                otherPath+='.txt'
            with open(otherPath,'w')as f:
                f.writelines(content_new)

except PermissionError:
    g.msgbox('程序终止！','提示')
