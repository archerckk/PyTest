'''
1.设置一个已经存在的密码
2.校验这个密码是否正确
3.一共只有3次机会去输入
4.密码包含*号的话不减少输入次数
5.不包含*号输入错误之后次数减少1次,提示重新输入：
6.输入正确的密码显示'密码正确，程序正在进入'
'''

password='test'
times=3

while times:
    tmp = input('请输入你的密码：')
    if tmp==password:
        print('密码正确!程序正在进入……')
        break
    elif '*' in tmp:
        print('密码中不能包含*号！你还有%d次机会!：' % times,end='')
        continue
    else:
        print('你输入的密码不正确！你还有%d次机会!：' % (times-1),end='')
    times -= 1


