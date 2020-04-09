import re


with open('resources/xmind.txt')as  f:
    content=f.readlines()

family_reg = re.compile(r'font-family="(.+?)"( )?')
new=[]
for i in content:

    if 'font-family'in i :
        result=family_reg.search(i).group(1)
        if "fo" not in result:
            new.append(i.replace(result,'Microsoft YaHei'))

            # print(i)
    else:
        new.append(i)
#
with open('resources/xmind_new.txt','w')as f:
    f.writelines(new)