import easygui as g
result=g.filesavebox(msg='文件保存',default='./',filetypes=['*.dll','dll文件'])
print(result)