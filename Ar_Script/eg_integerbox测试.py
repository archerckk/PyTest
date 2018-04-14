import easygui as g

result=g.integerbox(msg='请输入1-10个字符',lowerbound=1,upperbound=10,title='条件限制输入框')
print(result)