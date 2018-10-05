from email.header import Header
from email import encoders
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


'发送邮件服务器'
smtp_server='smtp.sina.cn'

'发送邮箱用户名/密码'
user_send='archerbin@sina.cn'
user_pwd='archer3203589'

'发送邮箱'
sender_email='archerbin@sina.cn'

'接收者邮箱'
receiver_email='501824353@qq.com'

'发送主题部分'
subject='这是一个测试邮件'

msg=MIMEMultipart()
msg['subject']=subject
msg['from']=sender_email
msg['to']=receiver_email

send_file=open('result/result.txt','rb').read()

#正文部分内容
msg.attach(MIMEText(
    '这是正文部分内容：test','plain','utf-8')
)

att=MIMEText(send_file,'base64','utf-8')
#这是一个未知类型的二进制文件
att['Content-Type']='application/octet-scream'
att['Content-Disposition']='attachment; filename="result.txt"'
msg.attach(att)

'邮件发送'
smtp=smtplib.SMTP(smtp_server)
smtp.login(user_send,user_pwd)
smtp.sendmail(sender_email,receiver_email,msg.as_string())
smtp.quit()


