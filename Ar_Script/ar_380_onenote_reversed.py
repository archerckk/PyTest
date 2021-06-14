with open('target.txt')as f:
    content=f.readlines()

content=reversed(content)
new_content=[]
for i in content:
    start,end=i.split('.')
    new_content.append(end)

with open('result.txt','w')as f:
    f.writelines(new_content)