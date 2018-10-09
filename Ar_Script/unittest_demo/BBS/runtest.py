import unittest
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerCN import HTMLTestReportCN
import os
import time
from email.mime.multipart import MIMEMultipart


def send_email(report, subject='测试报告'):
    '发送邮件服务器'
    smtp_server = 'smtp.sina.cn'

    '发送邮箱用户名/密码'
    user_send = 'archerbin@sina.cn'
    user_pwd = 'archer3203589'

    '发送邮箱'
    sender_email = 'archerbin@sina.cn'

    '接收者邮箱'
    receiver_email = '501824353@qq.com'

    with open(report, 'rb')as f:
        msg = f.read()
        filename = report.split(os.sep)[-1]
        print(type(msg))
        print(msg)

    '测试代码'
    # msg='<html><h1>这是测试内容!</h1></html>'
    # msg=MIMEText(content,'html','utf-8')
    # msg['Subject']='QQ邮箱自动化测试结果'
    # msg['From']='archerbin@sina.cn'
    # msg['To']='501824353@qq.com'

    '发送内容，头部信息配置'
    content = MIMEMultipart()

    content['Subject'] = Header(subject, 'utf-8')

    '''
    假如没有加from，to这两个字段的内容的话，会报错
    smtplib.SMTPDataError: (553, 'Envolope sender mismatch with header from..')
    '''
    content['From'] = sender_email
    content['To'] = receiver_email

    report_content = MIMEText(msg, 'html', 'utf-8')
    content.attach(report_content)

    att=MIMEText(open(report,'rb').read(),'text/html','utf-8')
    att['Content-Type']='application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=%s'%filename
    content.attach(att)


    '初始化邮件对象并发送邮件'
    mail_server = smtp_server
    smtp = smtplib.SMTP(mail_server, 25)
    b = smtp.login(user_send, user_pwd)
    a = smtp.sendmail(sender_email, receiver_email, content.as_string())
    smtp.quit()


def new_report(file_path):
    file_list = os.listdir(file_path)
    file_list.sort(key=lambda fn: os.path.getctime(file_path))
    file_new = os.path.join(file_path, file_list[-2])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_file = os.getcwd() + os.sep + 'report' + os.sep + now + '_result.html'


    file = open(report_file, 'wb')
    # runner = HTMLTestRunner(
    #     stream=file,
    #     title='QQ邮箱登录自动化测试报告',
    #     description='运行环境WIN10 谷歌浏览器'
    # )
    runner=HTMLTestReportCN(
        stream=file,
        title='QQ邮箱登录自动化测试报告',
        description='运行环境WIN10 谷歌浏览器'
    )
    discover = unittest.defaultTestLoader.discover(start_dir='./test_case', pattern='*sta.py')
    runner.run(discover)
    file.close()
    new_file = new_report(os.getcwd() + os.sep + 'report')
    # test_file=os.getcwd()+os.sep+'report'+os.sep+'2018_10_09_16_01_26result.html'
    send_email(new_file)
