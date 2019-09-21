#encoding=utf-8
import linecache
import time

data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

'生成每一个参数的字典属性顺序字典'
keys={data_keys[i]:i for i in range(len(data_keys))}

'读取目标文档的所有行，并且生成列表'
f=linecache.getlines('resources/twitter数据挖掘片段.txt')

'将'
lines=[line.split('","') for line in f ]

now=time.time()
print(now)
# for i in lines:
#     print(i)


#1.该文本里，有多少个用户。（要求：输出为一个整数。）
userCountSet=set([line[keys['username']] for line in lines])

userNum=len(userCountSet)
print('总的用户数量为：',userNum,'\n')


#2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
userList=list(userCountSet)
print('用户名称列表信息为：',userList,'\n')

#3 有多少个2012年11月发布的tweets
#created_at
#获取所有创建于2012年11月的的tweets
tweets_2012_11=filter(lambda line:line[keys['created_at']].split(' ')[0].startswith('2012-11'),lines)
# for i in tweets_2012_11:
#     print(i)
tweets_2012_11_Num=len(list(tweets_2012_11))
print('2012年11月创建了{}个tweets\n'.format(tweets_2012_11_Num))


#4 该文本里，有哪几天的数据？
#获取所有有发布微博的日期
dayTweets=list(set([line[keys['created_at']].split(' ')[0]for line in lines]))
dayTweets.sort()
print("发布日期的微博日期有：{}\n".format(dayTweets))


#5 该文本里，在哪个小时发布的数据最多？
#创建时间所有的微博信息获取到，生成一个小时数的字典，属于这个小数里面发布的数字就加1，排序该字典的值

hoursLine=([int(line[keys['created_at']][11:13]) for line in lines])
hoursList=[(hour,hoursLine.count(hour))for hour in range(24)]
hoursList.sort(key=lambda k:k[1],reverse=True)
print(hoursList)
print('{}时发布的数据最多\n'.format(hoursList[0][0]))


#6 该文本里，输出在每一天发表tweets最多的用户
#每一天的微博获取到，统计这一天发布tweets最多的用户
dayDict={day:dict() for day in dayTweets}

for line in lines:
    dayTime=line[keys['created_at']].split(' ')[0]
    username=line[keys['username']]

    if  username in  dayDict[dayTime].keys():
        dayDict[dayTime][username]+=1
    else:
        dayDict[dayTime][username]=1

for k,v in dayDict.items():
    tmpList=list(v.items())
    tmpList.sort(key=lambda k:k[1],reverse=True)
    dayDict[k]={tmpList[0][0]:tmpList[0][1]}

print("每一天发表tweets最多的用户显示为：{}\n".format(dayDict.items()))


#7 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率
#需要获取到每个小时发布的微博的数量，对于统计完的信息进行列表排序，返回0-24的结果显示列表

line_2012_11_03=list(filter(lambda line:line[keys['created_at']].split(' ')[0].startswith('2012-11-03'),lines))
'找出11-3号的所有微博'

hourDict_11_03={str(hour):0 for hour in range(0,24)}

for line in line_2012_11_03:
    hour=line[keys['created_at']][11:13]
    hourDict_11_03[str(int(hour))]+=1
    #解决00小时的问题

hourList_11_03=list(hourDict_11_03.items())

hourList_11_03.sort(key=lambda k:int(k[0]))
#解决字符串数字排序乱序问题

print("每个小时的发布tweets的频率为{}\n".format(hourList_11_03))


# print(line_2012_11_03)

#8 统计该文本里，来源的相关信息和次数
#发布微博的来源倒序显示出来
#生成一个source字典

sourceDict={line[keys['source']]:0 for line in lines}

for line in lines:
    source=line[keys['source']]
    sourceDict[source]+=1

sourceList=list(sourceDict.items())

sourceList.sort(key=lambda k:k[1],reverse=True)

print("来源的相关信息和次数如下：{}\n".format(sourceList))


#9 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个
#rt_v_url
rtUrl=filter(lambda line:line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta'),lines)
rtNum=len(list(rtUrl))
print("转发URL中有{}个已特定的前缀开头".format(rtNum))

#10 UID为573638104的用户 发了多少个微博

#11 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

#12 该文本里，谁发的微博内容长度最长
#content


#13 该文本里，谁转发的URL最多
#rt_num

#14 该文本里，11点钟，谁发的微博次数最多。

#15 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
#v_url