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
    with open(file,'rb')as f:
        content=f.read()

    '邮件头部信息'
    msg=MIMEText(content,'html','utf-8')
    msg['Subject']='自动测试结果'
    msg['From']='archerbin@sina.cn'
    msg['To']='501824353@qq.com'

    '发送邮件'
    smtp=smtplib.SMTP('smtp.sina.cn',25)
    smtp.login('archerbin@sina.cn','archer3203589')
    smtp.sendmail('archerbin@sina.cn','501824353@qq.com',msg.as_string())
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
