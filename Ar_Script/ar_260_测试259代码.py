# coding=gbk

import re
from ar_259_����_��������ȷ�Ͻű� import get_cf_conf as cf

with open('log.txt', 'r', encoding='utf-8')as f:
    log = f.read()
    # cf('com.pika.camera.android')
    # reg_ne = re.compile(r'http://stt.%s.+/ne' % 'com.q.photo.editor.android', re.I)
    reg_daily = re.compile(r'({("g_act":"daily_active")(.+)"g_cnt":1})', re.I)
    # reg_cashSDK_cf = re.compile(r'((http://cf.(.+?)\..+moduleid=3300&.+%s.+)|(http://.+?)\..+moduleid=3300&.+%s.+)' %('com.copohoroscope.china','com.copohoroscope.china') , re.I)
    reg_cashSDK_cf = re.compile(r'(http://cf.(.+)\..+moduleid=3300&.+%s.+)|(http://(.+)\..+moduleid=3100&.+%s.+)' %('com.q.photo.editor.android','com.q.photo.editor.android'), re.I)
    reg_ne = re.compile(r'(http://stt.%s.+/nw/ne)|(http://.+)/nw/ne' % 'qphotoeditor', re.I)

    try:
        # reg_ne_str = reg_ne.search(log).group()
        # print(reg_daily.search(log).group(2))
        print(reg_cashSDK_cf.search(log).group())
        print(reg_ne.search(log).group())
        # print('\n�¼�����ϱ�������֤�ɹ���', reg_ne_str)
    except:
        print('\n�¼�����ϱ�������֤ʧ��')
