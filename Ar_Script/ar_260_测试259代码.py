# coding=gbk

import re

with open('log.txt', 'r', encoding='utf-8')as f:
    log = f.read()
    reg_ne = re.compile(r'http://stt.%s.+/ne' % 'qphotoeditor', re.I)
    try:
        reg_ne_str = reg_ne.search(log).group()
        print('\n事件打点上报域名验证成功：', reg_ne_str)
    except:
        print('\n事件打点上报域名验证失败')
