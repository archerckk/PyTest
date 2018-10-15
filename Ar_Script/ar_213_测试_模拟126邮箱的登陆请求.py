import requests as r

'定义基础参数'
url='https://mail.126.com'
cookie="""
starttime=; nts_mail_user=archerckk@126.com:-1:1; df=mail126_letter; mail_upx=t2gd.mail.126.com|t3gd.mail.126.com|t4gd.mail.126.com|t1gd.mail.126.com|t2bj.mail.126.com|t3bj.mail.126.com|t4bj.mail.126.com|t1bj.mail.126.com; mail_upx_nf=; mail_idc=; Coremail=e799508b45379%yARdvDYxCKLHtnCFqUxxWJUyjwrULtKs%g4a42.mail.126.com; MAIL_MISC=archerckk@126.com; cm_last_info=dT1hcmNoZXJja2slNDAxMjYuY29tJmQ9aHR0cHMlM0ElMkYlMkZtYWlsLjEyNi5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRHlBUmR2RFl4Q0tMSHRuQ0ZxVXh4V0pVeWp3clVMdEtzJnM9eUFSZHZEWXhDS0xIdG5DRnFVeHhXSlV5andyVUx0S3MmaD1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEeUFSZHZEWXhDS0xIdG5DRnFVeHhXSlV5andyVUx0S3Mmdz1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSZsPS0xJnQ9LTEmYXM9dHJ1ZQ==; MAIL_SINFO=1539561858|0|#3&80#|archerckk@126.com; MAIL_PINFO=archerckk@126.com|1539561858|0|mail126|00&99|gud&1539391520&mail126#gud&440100#10#0#0|&0|mail126|archerckk@126.com; secu_info=1; mail_entry_sess=69cae7d26fcf28f3c0edaf0e758ea0b7a236adaef0274521d8b9bf5810279932316d7844266a9b855d9f388d42028e279dc6f1585990bb8a365849e8aa5245ff011e55914d4fbcfabee1398c27666021137b4c9d2a5fce94b775f01ca7a101450b333f3743e86e5b9338d17e089a53ea9f3381b47510195e541c3b34efb117bba665f5fddcd1c8cbdbb41ff9ba1b298f950301c24349323341257d3ee8f9db6e24da6e90fc16e5a571f4b37ff180b0af2b1b15151f7f8503da1cd5f2f76f5da4; locale=; Coremail.sid=yARdvDYxCKLHtnCFqUxxWJUyjwrULtKs; mail_style=js6; mail_uid=archerckk@126.com; mail_host=mail.126.com; MailMasterPopupTips=1539561865607; JSESSIONID=2102B6075F237E57F1864C72338A829D; _pk_id.16.3540=04b68ed3a8e833bf.1539561913.1.1539561913.1539561913.; _pk_ses.16.3540=*; ANTICSRF=cleared; NTES_SESS=wAVa7gA1_rlVcdCgraKlTNmkqBF8XGVBoEq1rqXBxTKaj0mKjiCG5_mzItf3hL8YLD_7oEa63OfVaOGOaPJ3XsOwjrHkO5N.Sp0iKBtJifuyqqOMxIAT7q3z7Zvof_LrZcVOwtA8Go.HHvM1s11hDbMHmlYEtUa4DRnqBnXSUGnI0kHiPPix7.8QD2oHVpEnx33o7gNhiZnxv57UPBMtXwAYl; S_INFO=1539561941|0|#3&80#|archerckk@126.com; P_INFO=archerckk@126.com|1539561941|0|mail126|00&99|gud&1539561858&mail126#gud&440100#10#0#0|&0|mail126|archerckk@126.com
"""
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

form_data={
    'User-Agent':user_agent,
    'cookie':cookie
}

request=r.post(url,data=form_data)
print(request.status_code)
