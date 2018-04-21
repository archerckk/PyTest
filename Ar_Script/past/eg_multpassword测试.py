import easygui as g
result=g.multpasswordbox(msg='请输入你的账号密码：',title='注册信息',fields=['账号：','密码：'])
print(result)