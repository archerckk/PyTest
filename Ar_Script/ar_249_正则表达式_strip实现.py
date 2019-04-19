import re

"""
1、只传入了一个参数，没有其他参数，去除前后的空格字符
2、传入第二个参数，去除传入参数的内容字段

"""

def reg_strip(str1,target=''):
    new_str = ''
    if target!='':
        target_reg=re.compile(r"(%s+)"%target)
        target_ruslt=target_reg.search(target)
        if target_reg==None:
            new_str=str1
        else:
            str1=str1.replace(target_ruslt.group(1),'')
            new_str=str1
    else:
        space_reg = re.compile(r"(\s*)(\d*\w*)(\s*)")
        result = space_reg.search(str1)
        group1 = result.group(1)
        group2 = result.group(2)
        group3 = result.group(3)

        if result.group(1) != '':
            group1 = ''
            print('group1为：', group1)
        if result.group(3) != '':
            group3 = group3.replace(' ', '')
            print('group3为：', group3)
        if group1 == '' and group3 == '':
            new_str = group2
            # print(new_str)
    return new_str
str1=' 12345435435fdfdgfdsscsssa '
target='ss'
print(reg_strip(str1))