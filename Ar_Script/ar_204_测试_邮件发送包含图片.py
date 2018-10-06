import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage



'''
1.邮件的基本参数定义
2.定义一个兼容html图片背景的对象
3.定义一个能兼容普通文本和超文本的对象
4.将图片的内容读取到，然后放进去超文本对象
5.将包含了图片内容的对象加到兼容html图片背景的对象
6.发送兼容html对象邮件
'''


#'定义邮件的基本参数'
'发送服务器'
smtp_server='smtp.sina.cn'

'登陆账号'
user_name='archerbin@sina.cn'
user_psw='archer3203589'

'接收者账号'
receiver='501824353@qq.com'

#文件头部内容
msg_main=MIMEMultipart('related')
subject='这是一个图片发送测试邮件'
# msg_main['Subject']=Header(subject,'utf-8')
# msg_main['From']=Header('测试邮件组','utf-8')
# msg_main['To']=Header('结果接收组','utf-8')

msg_main['Subject']=subject
msg_main['From']=user_name
msg_main['To']=receiver


#正文内容
msg_content=MIMEMultipart('alternative')

'html的a标签href链接假如是链接地址的话记得加[http://]输入完整的地址'
msg="""
<html>
<p>这是一个测试地址</p>
<p><a href='http://www.baidu.com'>请点击测试地址</a></p>
<p><image src='cid:image1'></p>
<p>来至：测试邮件组</p>
</html>
"""
msg_txt=MIMEText(msg,'html','utf-8')

msg_content.attach(msg_txt)

#将图片信息加载到头部
image_rb=open('result/喵喵测试.jpg','rb')
image=MIMEImage(image_rb.read())
image_rb.close()

image.add_header('Content-ID','<image1>')
msg_main.attach(image)
msg_main.attach(msg_content)

#发送邮件相关操作
try:
    smtp=smtplib.SMTP(smtp_server,25)
    smtp.login(user_name,user_psw)
    smtp.sendmail(user_name,receiver,msg_main.as_string())
    print('发送成功')
    smtp.quit()
except smtplib.SMTPException:
    print('发送失败')


