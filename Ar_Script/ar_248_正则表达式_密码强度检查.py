import re

"""
1、长度不少于8个字符
2、包含大写
3、包含小写字符
4、至少有一个数字
"""

#正则表达式检测
len_reg=re.compile(r'.{8,}')
lower_reg=re.compile(r'[a-z]+')
uper_reg=re.compile(r'[A-Z]+')
num_reg=re.compile(r'\d+')

#密码输入
toast = '请输入你的密码：'
while True:
    print(
    """
你的密码长度至少为8位，包含大写字母，小写字母和数字
    """)
    password=input(toast)
    len_result=len_reg.search(password)
    lower_result=lower_reg.search(password)
    uper_result=uper_reg.search(password)
    num_result=num_reg.search(password)

    if len_result==None:
        toast='你输入的密码长度少于8位：'
    elif lower_result==None:
        toast='你输入的密码不包含小写字母：'
    elif uper_result==None:
        toast='你输入的密码不包含大写字母：'
    elif num_result==None:
        toast='你输入的密码不包含数字：'
    else:
        print('\n设置密码成功！')
        break