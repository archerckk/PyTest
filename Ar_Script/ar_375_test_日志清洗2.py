import re
import pprint
import json

content=''

while 1:
    with open('text.txt')as f:
        for i in f:
            content += i
    mode=input('请选择你的模式:')
    reg_break=re.compile(r'2020-.+com.social.nene I/LovU: ')
    tmp_content=re.sub(reg_break,'',content)
    new_content=tmp_content.replace(' ','').replace('\n','')
    if mode=='1':
        try:
            json_result = json.loads(new_content)
            pprint.pprint(json_result)
        except Exception as e:
            print(e)
    else:
        print(new_content)


# with open('resources/text.txt','w')as f:
#     f.write(new_content)
