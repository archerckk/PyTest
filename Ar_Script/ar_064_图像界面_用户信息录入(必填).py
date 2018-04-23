import sys
import easygui as g

# '第一版本'
# while 1:
#     msg = '''
# 【*用户名为必填项。】
# 【*真实姓名为必填项。】
# 【*手机号码为必填项。】
# 【*E-mail为必填项。】
#     '''
#     title = '账号中心'
#     choices = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail']
#
#     result=g.multenterbox(msg,title,choices)
#     if '' in [result[0],result[1],result[3],result[5]]:
#         g.msgbox('存在*必填项为空，请重新填写！','提示')
#     else:
#         g.msgbox('注册成功！','提示')
#         break


#尝试写参考版本（）

# while 1:
#
#     msg = '请输入联系方式：'
#     choices = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail']
#     title = '账号中心'
#     # result=[]
#     result = g.multenterbox(msg, title, choices)
#
#     if result == None:
#         break
#     errmsg = ''
#     for i in range(len(choices)):
#         option = choices[i].strip()
#         if result[i].strip() == "" and option[0] == "*":
#             errmsg += ('【%s】为必填项。\n\n' % choices[i])
#     if errmsg == "":
#         break
#     result = g.multenterbox(errmsg, title, choices, result)
# print(result)


msg = '请输入你的联系方式:'
title = '账号中心'
choices = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail']

result = g.multenterbox(msg, title, choices)

while 1:

    if result==None:
        break

    errmsg=''

    for i in range(len(choices)):
        option=choices[i].strip()
        if result[i].strip()==''and option[0]=='*':
            errmsg+=('【%s】为必填项。\n\n'%choices[i])

    if errmsg=='':
        break

    result=g.multenterbox(errmsg,title,choices,result)
print('你的注册资料为：'+str(result))



# 参考答案
# import easygui as g

# msg = "请填写以下联系方式"
# title = "账号中心"
# fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
# fieldValues = []
# fieldValues = g.multenterbox(msg, title, fieldNames)
#
# while 1:
#     # 假如返回值为空，则为用户取消操作
#     if fieldValues == None:
#         break
#     errmsg = ""
#     # 遍历选项列表，将带‘*’的选项选出来
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == "" and option[0] == "*":
#             errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
#     if errmsg == "":
#         break
#     fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
#
# print("用户资料如下：%s" % str(fieldValues))
