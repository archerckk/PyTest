import easygui as g

result=g.multenterbox(msg='请输入你要输入的内容：',title='多输入框测试',fields=['姓名：','性别：'])
print(result)