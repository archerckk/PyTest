import easygui as g
result=g.fileopenbox(msg='文件打开测试',default='./*.py',filetypes=[['*.pkl','pickle类型'],'*.txt',['*.py','py格式']])
print(result)