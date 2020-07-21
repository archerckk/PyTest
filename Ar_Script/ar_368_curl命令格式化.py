import easygui

while 1:
    content=easygui.enterbox(msg='请输入你的curl命令：',title='curl命令格式化')
    content=content.replace('^','').replace('\n','').replace(' --compressed','')
    print(content)
