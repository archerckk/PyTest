# coding=gbk

import re
from ar_259_测试_上线域名确认脚本 import get_cf_conf as cf

with open('log.txt', 'r', encoding='utf-8')as f:
    log = f.read()
    cf('com.pika.camera.android')
    reg_ne = re.compile(r'http://stt.%s.+/ne' % 'qphotoeditor', re.I)
    reg_daily = re.compile(r'({("g_act":"daily_active")(.+)"g_cnt":1})', re.I)
    try:
        # reg_ne_str = reg_ne.search(log).group()
        print(reg_daily.search(log).group(2))
        # print('\n事件打点上报域名验证成功：', reg_ne_str)
    except:
        print('\n事件打点上报域名验证失败')
