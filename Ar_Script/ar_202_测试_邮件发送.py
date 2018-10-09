import smtplib
from email.mime.text import MIMEText
from email.header import Header

'发送邮件服务器'
smtp_server='smtp.sina.cn'

'发送邮箱用户名/密码'
user_send='archerbin@sina.cn'
user_pwd='archer3203589'

'发送邮箱'
sender_email='archerbin@sina.cn'

'接收者邮箱'
receiver_email='501824353@qq.com'

'发送主题'
subject='这是一个测试邮件'


'发送内容'
content=MIMEText('<html><h1>这是测试内容!</h1></html>','html','utf-8')
content['Subject']=Header(subject,'utf-8')

'''
假如没有加from，to这两个字段的内容的话，会报错
smtplib.SMTPDataError: (553, 'Envolope sender mismatch with header from..')
'''
content['From'] = sender_email
content['To'] = receiver_email

'发送邮件'
smtp=smtplib.SMTP(smtp_server,25)
# smtp.connect(smtp_server)
a=smtp.login(user_send,user_pwd)
abc=smtp.sendmail(sender_email,receiver_email,content.as_string())
smtp.quit()
