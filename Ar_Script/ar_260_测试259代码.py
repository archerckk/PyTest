# coding=gbk

import re

with open('log.txt', 'r', encoding='utf-8')as f:
    log = f.read()
    reg_ne = re.compile(r'http://stt.%s.+/ne' % 'qphotoeditor', re.I)
    try:
        reg_ne_str = reg_ne.search(log).group()
        print('\n�¼�����ϱ�������֤�ɹ���', reg_ne_str)
    except:
        print('\n�¼�����ϱ�������֤ʧ��')
