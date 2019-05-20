#encoding=utf-8

import logging
import os
import unittest
from  ar_265_测试_自动检测星座接口 import  DailyTest
import time
from HTMLTestRunnerCN import HTMLTestReportCN
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from BeautifulReport import BeautifulReport as bf

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
suite = unittest.TestSuite()
suite.addTest(DailyTest('testChinaApi'))
suite.addTest(DailyTest('testEnglishApi'))
now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())

fileName = os.getcwd() + os.sep + 'result' + os.sep + 'HoroscopesApiTest_' + now + '.html'
logging.debug('报告路径为：', fileName)

file = open(fileName, 'wb')

runner=bf(suite)
# runner = HTMLTestReportCN(
#     stream=file,
#     title='星座中文接口&星座英文接口数据返回测试报告',
#     description='星座接口测试用例执行情况：'
# )
runner.report(filename=os.sep + 'result' + os.sep + 'HoroscopesApiTest_' + now + '.html',description='星座接口测试用例执行情况：')
file.close()
time.sleep(2)

smtpServer='smtp.avazu.net'
smtpAccount='zhibin.chen@dotcunited.com'
smtpPsw='Chenzhibin2019'
target_list=[]
with open('mailList.txt')as f:
    for i in f:
        target_list.append(i)

message=MIMEMultipart()
message['from']=Header('zhibin.chen@dotcunited.com','utf-8')
message['to']=Header(target_list[1],'utf-8')
message['subject']=Header('Re:星座中文接口和星座英文接口数据返回测试报告','utf-8')

sendFileContent=open(fileName,'rb').read()

'发送附件构造'
att=MIMEText(sendFileContent,'base64','utf-8')
#这是一个未知的类型
att['Content-Type']='application/octet-scream'
att['Content-Disposition']='attachment; filename=%s'%fileName
message.attach(att)

'发送文本内容构造'
att2=MIMEText(open(fileName,'rb').read(),'html','utf-8')
message.attach(att2)

'邮件发送'
try:
    smtp=smtplib.SMTP(smtpServer)
    smtp.login(smtpAccount,smtpPsw)
    smtp.sendmail(smtpAccount,target_list[1],message.as_string())
    smtp.quit()
except smtplib.SMTPException:
    print('发送失败')