'''
1.设置一个已经存在的密码
2.校验这个密码是否正确
3.一共只有3次机会去输入
4.密码包含*号的话不减少输入次数
5.不包含*号输入错误之后次数减少1次,提示重新输入：
6.输入正确的密码显示'恭喜你，登录成功！'
'''
# target='test'
# times=3
# while times:
#     psw = input('请输入你的密码：')
#     if psw==target:
#         print('恭喜你，登录成功！')
#         break
#     elif psw.isspace()or len(psw)==0:
#         print('你输入的密码不能为空！',end='')
#     elif '*'in psw:
#         print('你输入的密码不能包含【*】号！',end='')
#     else:
#         times-=1
#         if times==0:
#             print('你的尝试次数已用完！禁止登录')
#         else:
#             print('你输入的密码不正确！你还有%d次机会！' % times, end='')


#参考答案
password="test"
times=3
while times:
    tmp = input("请输入你的密码:")
    if password == tmp:
        print("密码正确，进入程序……")
        break
    elif "*" in tmp:
        print("你的输入不能包含'*'号！你还有" + str(times) + "机会", end="")
        # continue
    else:
        print("你的密码不正确!你还有" + str(times-1) + "机会", end="")
        times -= 1