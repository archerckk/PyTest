from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerCN import HTMLTestReportCN
from email.mime.text import MIMEText
import smtplib
import os
import unittest
import time


"定义运行脚本"
def file_sort(test_report):
    report_lists=os.listdir(test_report)
    report_lists.sort(key=lambda fn:os.path.getctime(test_report))
    report=os.path.join(test_report,report_lists[-1])
    print(report)
    return report



'邮件发送'
def send_email(file):
    '获取测试结果内容'
    '发送邮件服务器'
    smtp_server = 'smtp.sina.cn'

    '发送邮箱用户名/密码'
    user_send = 'archerbin@sina.cn'
    user_pwd = 'archer3203589'

    '发送邮箱'
    sender_email = 'archerbin@sina.cn'

    '接收者邮箱'
    receiver_email = '501824353@qq.com'

    '发送主题'
    subject = '自动测试结果'


    with open(file,'rb')as f:
        content=f.read()

    '邮件头部信息'
    msg=MIMEText(content,'html','utf-8')
    msg['Subject']=subject
    msg['From']=sender_email
    msg['To']=receiver_email

    '发送邮件'
    smtp=smtplib.SMTP(smtp_server,25)
    smtp.login(user_send,user_pwd)
    smtp.sendmail(sender_email,receiver_email,msg.as_string())
    smtp.quit()
    print('邮件发送成功')


if __name__ == '__main__':
    test_path = 'Test_case'
    report_path='Report'
    discover = unittest.defaultTestLoader.discover(start_dir=test_path,
                                                   pattern='test*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    file_name = report_path + os.sep + now+'_result.html'
    fp=open(file_name,'wb')
    # runner=HTMLTestReportCN(stream=fp,
    #                       title='测试报告',
    #                       description='用例执行情况'
    #                       )
    runner = HTMLTestRunner(stream=fp,
                              title='测试报告',
                              description='用例执行情况'
                              )
    runner.run(discover)
    fp.close()
    new_report=file_sort(report_path)
    send_email(new_report)
