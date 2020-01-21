from email.header import Header
from email import encoders
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import pdfkit
import subprocess
import os
import time
from selenium import webdriver
import logging as log

log.basicConfig(level=log.DEBUG,format='%(asctime)s-%()s-%()')


'发送邮件服务器'
smtp_server='smtp.dotcunited.com'

'发送邮箱用户名/密码'
user_send='zhibin.chen@dotcunited.com'
user_pwd='Chenzhibin2019'

'发送邮箱'
sender_email='zhibin.chen@dotcunited.com'

'接收者邮箱'
receiver_email='501824353@qq.com'

'发送主题部分'
subject='这是一个测试邮件'

msg=MIMEMultipart('related')
msg['subject']=subject
msg['from']=sender_email
msg['to']=receiver_email

driver=webdriver.Chrome()




send_file=open('testreport.html','r',encoding='utf-8').read()
htmlFile=os.getcwd()+os.sep+'testreport.html'

# driver.set_window_size(1280,900)
driver.get(htmlFile)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get_screenshot_as_file('./baidu.png')
time.sleep(2)
driver.quit()

htmlsmg="""<p><img src="cid:baidu.png"></p>"""
#
# command='wkhtmltoimage --width 1680 --height 900 %s tmp_result.jpg'%htmlFile

# handle=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)

# while True:
#     if handle.poll() != None:
#         print('进程已终止')
#         break
#     else:
#         continue

time.sleep(2)
#
htmlatt=MIMEMultipart('alternative')
msg.attach(htmlatt)


#正文部分内容
htmlatt.attach(MIMEText(htmlsmg ,'html','utf-8'))

#图片内容读取
imgfile=open('baidu.png','rb')
msgImage=MIMEImage(imgfile.read())
imgfile.close()

msgImage.add_header('Content-ID','<baidu.png>')
msg.attach(msgImage)


#附件添加
att=MIMEText(open('testreport.html','rb').read(),'base64','utf-8')
#这是一个未知类型的二进制文件
att['Content-Type']='application/octet-scream'
att['Content-Disposition']='attachment; filename="testreport.html"'
msg.attach(att)




'邮件发送'
smtp=smtplib.SMTP(smtp_server)
smtp.login(user_send,user_pwd)
smtp.sendmail(sender_email,receiver_email,msg.as_string())
smtp.quit()

#
