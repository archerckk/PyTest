#encoding=utf-8
import linecache
import time

data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

keys = {data_keys[k]:k for k in range(0,len(data_keys))}
print(keys.items())
now = time.time()


f = linecache.getlines('resources/twitter数据挖掘片段.txt')
# for i in f:
#     print(i)
print(type(f))
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


hours = [int(line[keys['created_at']][11:13]) for line in lines]

total_by_hour = [(h,hours.count(h)) for h in range(0,24) ]

total_by_hour.sort(key=lambda k:k[1],reverse=True)

max_hour = total_by_hour[0][0]

assert type(max_hour) == int

#6 该文本里，输出在每一天发表tweets最多的用户

dateline_by_user = {k:dict() for k in lines_by_created}

print(dateline_by_user)
for line in lines:
    dateline = line[keys['created_at']].split(' ')[0]
    username = line[keys['username']]
    if dateline_by_user[dateline].get(username):
        dateline_by_user[dateline][username] += 1
    else:
        dateline_by_user[dateline][username] = 1

for k,v in dateline_by_user.items():
    # print(k)
    us = list(v.items())
    us.sort(key=lambda k:k[1],reverse=True)
    dateline_by_user[k] = {us[0][0]:us[0][1]}


assert type(dateline_by_user) == dict


#7 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率
#需要获取到每个小时发布的微博的数量，对于统计完的信息进行列表排序，返回0-24的结果显示列表


lines_from_2012_11_03 = filter(lambda line:line[keys['created_at']].startswith('2012-11-03'),lines)
#获取到11-03号这一天发布的微博


hourlines_from_2012_11_03 = {str(i):0 for i in range(0,24)}
#生成0-24小时的的字典，默认值为0

for line in lines_from_2012_11_03:
    hour = line[keys['created_at']][11:13]
    hourlines_from_2012_11_03[str(int(hour))] += 1
#获取微博的发布的小时，并且将这小时数，作为键，对应的字典值加1

hour_timeline_from_2012_11_03 = [(k,v) for k,v in hourlines_from_2012_11_03.items()]
#将字典的item转换为列表

hour_timeline_from_2012_11_03.sort(key=lambda k:int(k[0]))
#根据地0个元素来排序
print(hour_timeline_from_2012_11_03)

assert type(hour_timeline_from_2012_11_03) == list


#8 统计该文本里，来源的相关信息和次数
#发布微博的来源倒序显示出来


source = set([k[keys['source']] for k in lines])
#获取lines里面的来源信息，并且去重
source_dict = {s:0 for s in source}
#生成一个source字典

for line in lines:
    source_name = line[keys['source']]
    source_dict[source_name] += 1
source_list = [(k,v) for k,v in source_dict.items()]
source_list.sort(key=lambda k:k[1],reverse=True)
print(source_list)
assert type(source_list) == list



#9 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个

umi_total = 0
for line in lines:
    if line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta'):
        umi_total += 1
assert type(umi_total) == int

#10 UID为573638104的用户 发了多少个微博

tweets_total_from_573638104 = 0
for line in lines:
    if line[keys['uid']] == '573638104' :
        tweets_total_from_573638104 += 1
assert type(tweets_total_from_573638104) == int


# 11 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

def get_user_by_max_tweets(*uids):
    '''
    @deprecated:参数可为字符串或者数字
    '''

    if len(uids) > 0:
        uids = filter(lambda u: type(u) == int or u.isdigit(), uids)
        uids = list(map(str, uids))
        if len(uids) > 0:
            uids_dict = {x: 0 for x in uids}
            for line in lines:
                uid = line[keys['uid']]
                if uid in uids:
                    uids_dict[uid] += 1
            uids_and_tweets_total = [(x, y) for x, y in uids_dict.items()]
            uids_and_tweets_total.sort(key=lambda k: k[1], reverse=True)
            return uids_and_tweets_total[0][0]
    return "null"


assert get_user_by_max_tweets() == 'null'
assert get_user_by_max_tweets('ab', 'cds') == 'null'
assert get_user_by_max_tweets('ab', 'cds', '123b') == 'null'
assert get_user_by_max_tweets('12342', 'cd') == '12342'
assert get_user_by_max_tweets('28803555', 28803555) == '28803555'
assert get_user_by_max_tweets('28803555', 28803555, '96165754') == '28803555'


#12 该文本里，谁发的微博内容长度最长

lines_by_content_length = [(line[keys['username']],len(line[keys['content']])) for line in lines]
lines_by_content_length.sort(key=lambda k:k[1],reverse=True)
user_by_max_content = lines_by_content_length[0][0]
# todo 如果有多个最多怎么办？
assert type(user_by_max_content) == str


#13 该文本里，谁转发的URL最多

lines_by_rt = [(line[keys['uid']],int(line[keys['rt_num']])) for line in lines if line[keys['rt_num']] != '']
lines_by_rt.sort(key=lambda k:k[1],reverse=True)
user_by_max_rt = lines_by_rt[0][0]
print(user_by_max_rt)
assert type(user_by_max_rt) == str

#14 该文本里，11点钟，谁发的微博次数最多。

lines_on_hour11 = filter(lambda line:line[keys['created_at']].startswith('11',11,13),lines)
lines_by_uid_on_hour11 = {k[keys['uid']]:0 for k in lines_on_hour11}
for line in lines_on_hour11:
    uid = line[keys['uid']]
    lines_by_uid_on_hour11[uid] += 1
d = [(k,v) for k,v in lines_by_uid_on_hour11.items()]
d.sort(key=lambda k:k[1],reverse=True)
uid_by_max_tweets_on_hour11 = d[0]
# todo 如果有多个最多怎么办？
print(uid_by_max_tweets_on_hour11)
# assert type(uid_by_max_tweets_on_hour11) == str


#15 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）

uid_by_v_url = {k[keys['uid']]:0 for k in lines}
for line in lines:
    uid = line[keys['uid']]
    if lines[keys['v_url']] != '':
        uid_by_v_url[uid] += 1
uid_sort_by_v_url = [(k,v) for k,v in uid_by_v_url.items()]
uid_sort_by_v_url.sort(key=lambda k:k[1],reverse=True)
uid_by_max_v_url = uid_sort_by_v_url[0]
print(uid_by_max_v_url)
# todo 如果有多个最多怎么办？
# assert type(uid_by_max_v_url) == str

print ('运算时间：%s'%(time.time() - now)) #整体运行时间