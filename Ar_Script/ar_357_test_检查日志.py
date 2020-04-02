import re

user_id_reg=re.compile(r'用户id为：(\d+)')
result=[]
with open('check_add_user',encoding='UTF-8')as f:
    for i in f:
        if '策略用户成功获取'in i :
            text=user_id_reg.search(i).group(1)
            result.append(text)

length1=len(result)
length2=len(set(result))

assert length1==length2