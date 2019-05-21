#encoding=utf-8

import logging
import os
import unittest
from  ar_265_测试_自动检测星座接口 import  DailyTest
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
from BeautifulReport import BeautifulReport as bf
from selenium import webdriver

os.chdir(os.getcwd())
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

'测试集脚本配置'
suite = unittest.TestSuite()
suite.addTest(DailyTest('testChinaApi'))
suite.addTest(DailyTest('testEnglishApi'))
now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())

fileName = os.getcwd() + os.sep + 'result' + os.sep + 'HoroscopesApiTest_' + now + '.html'
logging.debug('报告路径为：', fileName)

file = open(fileName, 'wb')


# runner = HTMLTestReportCN(
#     stream=file,
#     title='星座中文接口&星座英文接口数据返回测试报告',
#     description='星座接口测试用例执行情况：'
# )
runner=bf(suite)
runner.report(filename=os.sep + 'result' + os.sep + 'HoroscopesApiTest_' + now + '.html',description='星座接口测试用例执行情况：')
file.close()
time.sleep(2)

'图片截图生成'
screenShot='./result/rusultScreenShot_%s.png'%now

driver=webdriver.Chrome()
driver.get(fileName)
driver.maximize_window()
driver.implicitly_wait(5)
'控制页面滑动到底部'
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
'截图'
driver.get_screenshot_as_file(screenShot)
time.sleep(2)
driver.quit()

'邮件参数设置'
smtpServer='smtp.avazu.net'
smtpAccount='zhibin.chen@dotcunited.com'
smtpPsw='Chenzhibin2019'
target_list=[]
with open('mailList.txt')as f:
    for i in f:
        target_list.append(i)

'邮件的基础参数'
message=MIMEMultipart('related')
message['from']=smtpAccount
message['to']=Header(target_list[1],'utf-8')
message['subject']=Header('Re:%s_星座中文接口和星座英文数据返回接口测试报告'%now,'utf-8')



'发送附件构造'
sendFileContent=open(fileName,'rb').read()
att=MIMEText(sendFileContent,'base64','utf-8')
#这是一个未知的类型
att['Content-Type']='application/octet-scream'
att['Content-Disposition']='attachment; filename=%s'%fileName
message.attach(att)

'发送文本内容构造'
msg_alterNative=MIMEMultipart('alternative')
message.attach(msg_alterNative)
mailMsg="""
<p><img src="cid:result"></p>
"""
msg_alterNative.attach(MIMEText(mailMsg,'html','utf-8'))

'图片对象构造'
image=open(screenShot,'rb')
mimeImage=MIMEImage(image.read())
image.close()
'添加图像ID，让'
mimeImage.add_header('Content-ID','<result>')
message.attach(mimeImage)


'邮件发送'
logging.debug('开始发送邮件')
try:
    smtp=smtplib.SMTP(smtpServer)
    smtp.login(smtpAccount,smtpPsw)
    smtp.sendmail(smtpAccount,target_list[1],message.as_string())
    smtp.quit()
    logging.debug('发送成功')
except smtplib.SMTPException:
    print('发送失败')