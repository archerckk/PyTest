# coding=gbk

import re
# from ar_259_测试_上线域名确认脚本 import get_cf_conf as cf

with open('log_test.txt', 'r', encoding='utf-8')as f:
    log = f.read()
    # cf('com.pika.camera.android')
    # reg_ne = re.compile(r'http://stt.%s.+/ne' % 'com.q.photo.editor.android', re.I)
    reg_daily = re.compile(r'({("g_act":"daily_active")(.+)"g_cnt":1})', re.I)
    # reg_cashSDK_cf = re.compile(r'((http://cf.(.+?)\..+moduleid=3300&.+%s.+)|(http://.+?)\..+moduleid=3300&.+%s.+)' %('com.copohoroscope.china','com.copohoroscope.china') , re.I)
    reg_cashSDK_cf = re.compile(r'(http://cf.(.+)\..+moduleid=3300&.+%s.+)|(http://(.+)/m/.+moduleid=3000&.+%s.+)' %('com.copohoroscope.china','com.copohoroscope.china'), re.I)
    reg_radicalSDK_cf = re.compile(r'(http://cf.(.+)\..+moduleid=3300&.+%s.+)|(http://(.+)/m/.+moduleid=3300&.+%s.+)' %('com.pika.camera.android','com.pika.camera.android'), re.I)
    reg_guidSDK_cf = re.compile(r'(http://cf.(.+)\..+moduleid=3300&.+%s.+)|(http://(.+)/m/.+moduleid=3100&.+%s.+)' %('com.pika.camera.android','com.pika.camera.android'), re.I)
    reg_ne = re.compile(r'(http://stt.%s.+/nw/ne)|(http://.+)/nw/ne' % 'qphotoeditor', re.I)

    reg_ne = re.compile(r'(http://stt.%s.+/nw/ne|http://\d+.+/nw/ne)' % 'copohoroscopechina', re.I)
    reg_adSDK_cf = re.compile(
        r'((http://mo.(.+)\..+)|(http://(.+))/(cr)/.+pkg_name=%s&.+has_sim=false.+)' % 'com.pika.camera.android', re.I)
    try:
        # reg_ne_str = reg_ne.search(log).group()
        # print(reg_daily.search(log).group(2))
        print(reg_ne.search(log).group())
        # print(reg_cashSDK_cf.search(log).group())
        # print(reg_radicalSDK_cf.search(log).group())
        # print(reg_guidSDK_cf.search(log).group())
        # print(reg_adSDK_cf.search(log).group())
        # print(reg_ne.search(log).group())
        # print('\n事件打点上报域名验证成功：', reg_ne_str)

    except:
        print('\n事件打点上报域名验证失败')
