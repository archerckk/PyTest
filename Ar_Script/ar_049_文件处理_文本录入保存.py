#encoding=gbk
print()
'''
��дһ�����򣬽����û������벢����Ϊ�µ��ļ������뱣��ָ��Ϊ��:w��
'''

filename=input('�����������ļ�����')
f=open('result/%s'%filename,'w')
print('���������ݡ���������":w"�����˳�����')
while 1:
    content = input()
    if content!=':w':
        f.write(content+'\n')
        #�ο���������f.write('%s\n' % write_some)
        #���е������������д��
    else:
        break

