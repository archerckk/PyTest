import re
import pprint
import json

content=''
with open('resources/text.txt')as f:
    for i in f:
        content+=i

reg_break=re.compile(r'2020-.+com.social.nene I/LovU: ')
tmp_content=re.sub(reg_break,'',content)
new_content=tmp_content.replace(' ','').replace('\n','')

json_result=json.loads(new_content)
pprint.pprint(json_result)

# with open('resources/text.txt','w')as f:
#     f.write(new_content)
