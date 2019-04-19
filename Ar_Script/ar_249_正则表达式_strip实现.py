import re

"""
1、只传入了一个参数，没有其他参数，去除前后的空格字符
2、传入第二个参数，去除传入参数的内容字段

"""

def reg_strip(str1,target=''):
    new_str = ''
    start_space = False
    end_space=False
    print('原字符串为：%s'%str1)
    if target=='':
        print('没有传入target参数，执行前后去空格')
        space_reg = re.compile(r"(\s*)(\d*\w*)(\s*)")
        result = space_reg.search(str1)
        group1 = result.group(1)
        group2 = result.group(2)
        group3 = result.group(3)

        if result.group(1) != '':
            group1 = ''
            print('检测到前面有空格占位')
            start_space = True
        if result.group(3) != '':
            group3 = group3.replace(' ', '')
            end_space = True
            print('检测到后面有空格占位')
        if group1 == '' and group3 == '' and start_space == False and end_space == False:
            new_str = group2
            print('内容前后不包含空格，显示原内容:%s' % new_str, end='')
        if group1 == '' and group3 == '' and (start_space == True or end_space == True):
            new_str = group2
            print('去除空格后的结果显示为:%s' % new_str, end='')
    else:
        print('执行关键字查询流程')
        target_reg = re.compile(r"(%s+)" % target)
        target_ruslt = target_reg.search(str1)

        if target_ruslt== None:
            new_str = str1
            print('没有查找到关键字，显示原文案:%s' % new_str)
        else:
            key_word = target_ruslt.group(1)
            print('找到关键字：%s,执行去除' % key_word)
            str1 = str1.replace(target_ruslt.group(1), '')
            new_str = str1
            print("去除的结果为：%s" % new_str)


    return new_str

str1=input('请输入你要测试的字符串：')
target=input('不输入则执行前后去空格，输入则去掉目标字符：')
print()
reg_strip(str1,target)