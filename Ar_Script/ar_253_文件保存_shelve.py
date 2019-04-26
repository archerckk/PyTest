import shelve

#数据储存
shefile=shelve.open('mydata')
cats=['test1','test2','test3']
shefile['cats']=cats
shefile.close()

#数据读取
shefile2=shelve.open('mydata')
print(shefile2['cats'])
print(shefile2.values())
for i in shefile2.values():
    for j in i:
        print(j)
shefile2.close()