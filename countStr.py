#encording=utf-8
keyWords='next|gosms|go_keyboard|goforandroid|3g.net.cn|GOSMS|GoKeyBoard|zcamera|PhotoEditor|beautycam|collagepe|GoMagicRecorder|GoMusic|GoBattery|GoSpeed|GoEmail|GoFlo|GoLanuncher|GomoAdSdk|GoMultiple|GONews|GOPlayer|GOPowerMaster|GoRealis|GORecorder|GOSafeBox|GOSecurity|GOTube|GOVideo|GoVpn|GOWeather|GOScreenRecorder|GoClock|GONetworkSecurity|GOToucher|GOColorJump|GoFileManager|GoLocker'
keyWords=keyWords.split('|')
file1=input('请输入你要检查的文件完整路径名字:')
file1.strip('"')
resultStr=''
sum=0
target_file=open(file1)
dict_result={}


for i in target_file:
    for each_key in keyWords:
        if each_key in i:
            dict_result.setdefault(each_key,0)
            sum+=i.count(each_key)
            dict_result[each_key]+=1


# # for i in target_file:
# #     sum+=i.count(target)
# for i in target:


print('统计结果如下:')
for i in dict_result.items():
    print(i)

input()