#输入一个数字，假如不为数字，则重新输入，假如输入为数字，则打印输入内容
str1=input('请输入一个数字：')
while not str1.isdigit():
    print('你输入的数字不是一个数字，请重新输入：',end='')
    str1=input()
print('你输入的为数字：'+str1)