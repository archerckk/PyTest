name=input('请输入待查找的用户名：')
score=[['迷途',85],['黑夜',80],['小布丁',65],['娃娃',95]]
isfind=False
for each in score:
    if each[0]==name:
        print(name+'得分是：',each[1])
        isfind=True
        break

if isfind==False:
    print('查找的数据不存在')
