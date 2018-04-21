import easygui as g

# judge=1
# def judge_null(tmp):
#     if tmp.isspace()or len(tmp)==0:
#        return judge==0
#
# while 1:
#     user_info=g.multenterbox(title='账号中心',
#                          msg='【*用户名】为必填项\t【*真实姓名】为必填项\t【*手机号码】为必填项\t【*E-mail】为必填项',
#                         fields=['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
#                )
#
#     if judge_null(user_info[0])==0:
#         g.msgbox(title='提示信息',msg='你输入的用户名为空')
#     elif judge_null(user_info[1])==0:
#         g.msgbox(title='提示信息',msg='你输入的真实姓名为空')
#     elif judge_null(user_info[3])==0:
#         g.msgbox(title='提示信息',msg='你输入的手机号码为空')
#     elif judge_null(user_info[5])==0:
#         g.msgbox(title='提示信息',msg='你输入的E-mail为空')
#     else:
#         g.msgbox(title='提示信息',msg='恭喜你注册成功')
#         break


#参考2
title='用户信息填写'
msg='请真实填写用户信息'
field_list=['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
field_value=[]
field_value = g.multenterbox(msg,title,field_list)

while 1:
    if field_value==None:
        break
    err_msg=''
    for i in range(len(field_list)):
        option=field_list[i].strip()
        if field_value[i].strip()==''and option[0]=='*':
            err_msg+='【%s】为必填项\n\n'%(field_list[i])
    if err_msg=='':
        break
    field_value = g.multenterbox(err_msg, title, field_list,field_value)

print('用户的资料如下：'+str(field_value))