import unittest
import smtplib
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner
import os
import time

def send_email(report):
    with open(report,'rb')as f:
        content=f.read()

    msg=MIMEText(content,'html','utf-8')
    msg['Subject']='QQ邮箱自动化测试结果'
    msg['From']='archerbin@sina.cn'
    msg['To']='501824353@qq.com'


    mail_server='smtp.sina.cn'
    smtp=smtplib.SMTP(mail_server,25)
    smtp.login('archerbin@sina.cn','archer3203589')
    smtp.sendmail('archerbin@sina.cn','chenzhibin@gomo.com',msg.as_string())
    smtp.quit()


def new_report(file_path):
    file_list=os.listdir(file_path)
    file_list.sort(key=lambda fn:os.path.getctime(file_path))
    file_new=os.path.join(file_path,file_list[-2])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now=time.strftime("%Y_%m_%d_%H_%M_%S")
    report_file=os.getcwd()+os.sep+'report'+os.sep+now+'result.html'

    file=open(report_file,'wb')
    runner=HTMLTestRunner(
        stream=file,
        title='QQ邮箱登录自动化测试报告',
        description='运行环境WIN10 谷歌浏览器'
    )
    discover = unittest.defaultTestLoader.discover(start_dir='./test_case',pattern='*sta.py')
    runner.run(discover)
    file.close()
    new_file=new_report(os.getcwd()+os.sep+'report')
    send_email(new_file)

