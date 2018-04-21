import easygui as g

user_info=g.multenterbox(title='账号中心',msg='【*用户名】为必填项\t【*真实姓名】为必填项\t【*手机号码】为必填项\t【*E-mail】为必填项',
               fields=['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
               )