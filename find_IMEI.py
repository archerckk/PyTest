# str1='''
#
#
# {"tags":"","reqs":[{"showquantity":0,"pageid":0,"moduleId":0}],"filterpkgnames":"","phead":{"entranceId":"1","model":"HTC D820t","hasmarket":1,"sys":"4.4.4","iscn":2,"dataChannel":"204","aid":"e9d1eba1fe333af9","net":"wifi","cversion":8,"pkgname":"com.voyagephotolab.picframe","lang":"en","cid":"212","cdays":2,"pversion":21,"requesttime":"2018-05-01 19:52:40","isvpn":2,"cversionname":"1.0","gadid":"9c085d08-f260-4747-aebc-305f95be6c5e","dpi":"720*1184","sdk":19,"local":"US","buychannel":"appflood","user_from":1,"channel":"101","goid":"1500118235188e9d1eba1fe333af9"}}
#
#
#
# '''
target=['"IMEI"','"imei"','"IMSI"','"imsi"','"email"','"emails"','"gmail"','"Gmail"']


str1=input()
tmp=str1.split(',')
result={}
for i in tmp:
  # print(i)
   try:
    (begin,end)=i.split(":")
    if begin in target:
        result.setdefault(begin,end)
   except ValueError:
       pass

for i in result:
    print(i,result[i])
