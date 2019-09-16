#encoding=utf-8
import linecache
import time

data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

keys = {data_keys[k]:k for k in range(0,len(data_keys))}
print(keys.items())
now = time.time()


f = linecache.getlines('resources/twitter数据挖掘片段.txt')

lines=[x[1:-1].split('","') for x in f]

# for i in lines:
#     print(i)

# for i in f:
#     print(i)

# print(f)

"1.该文本里，有多少个用户。（要求：输出为一个整数。）"
# txtFile=open('resources/twitter数据挖掘片段.txt',encoding='utf-8')
# numList=[]
# nameList=[]
# for i in txtFile.readlines():
#     try:
#         splitList=i.split(',')
#         # print(splitList)
#         for i in splitList[0]:
#             if i.strip('"').isdigit() :
#                 numList.append(i)
#
#     except UnicodeEncodeError:
#         pass
#
# totalNum=len(numList)
# print(totalNum)

users = set([line[keys['username']] for line in lines])

user_total = len(set(users))
# print(user_total)
assert type(user_total) == int




"2.该文本里，每一个用户的名字。 （要求：输出为一个list。）"
# txtFile2=open('resources/twitter数据挖掘片段.txt',encoding='utf-8')
#
# for i in txtFile2.readlines():
#     try:
#         splitList=i.split(',')
#         # print(splitList)
#         for i in splitList[2]:
#                 nameList.append(i)
#
#     except UnicodeEncodeError:
#         pass
# print(nameList)

users = list(users)
assert type(users)==list

#3 有多少个2012年11月发布的tweets

lines_from_2012_11 = list(filter(lambda line:line[keys['created_at']].startswith('2012-11'),lines))

lines_total_from_2012_11 = len(lines_from_2012_11)
print('正在打印3内容')
print(lines_total_from_2012_11)

# for i in list(lines_from_2012_11):
#     print(i)

assert type(lines_total_from_2012_11) == int


#4 该文本里，有哪几天的数据？

users_by_date = [line[keys['created_at']].split(' ')[0] for line in lines]

lines_by_created = list(set(users_by_date))

lines_by_created.sort()

print(lines_by_created)
assert type(lines_by_created) == list

#5 该文本里，在哪个小时发布的数据最多？
# todo 这里用time模块做时间转换最好。下例只为讲解拆分方法

hours = [int(line[keys['created_at']][11:13]) for line in lines]

total_by_hour = [(h,hours.count(h)) for h in range(0,24) ]

total_by_hour.sort(key=lambda k:k[1],reverse=True)

max_hour = total_by_hour[0][0]

assert type(max_hour) == int

#6 该文本里，输出在每一天发表tweets最多的用户

dateline_by_user = {k:dict() for k in lines_by_created}

for line in lines:
    dateline = line[keys['created_at']].split(' ')[0]
    username = line[keys['username']]
    if dateline_by_user[dateline].has_key(username):
        dateline_by_user[dateline][username] += 1
    else:
        dateline_by_user[dateline][username] = 1

for k,v in dateline_by_user.items():
    # print(k)
    us = v.items()
    us.sort(key=lambda k:k[1],reverse=True)
    dateline_by_user[k] = {us[0][0]:us[0][1]}

assert type(dateline_by_user) == dict