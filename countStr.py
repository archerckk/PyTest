target='next|gosms|go_keyboard|goforandroid|3g.net.cn|GOSMS|GoKeyBoard|zcamera|PhotoEditor"|beautycam|collagepe|GoMagicRecorder|GoMusic|GoBattery|GoSpeed|GoEmail|GoFlo|GoLanuncher|GomoAdSdk|GoMultiple|GONews|GOPlayer|GOPowerMaster|GoRealis|GORecorder|GOSafeBox|GOSecurity|GOTube|GOVideo|GoVpn|GOWeather|GOScreenRecorder|GoClock|GONetworkSecurity|GOToucher|GOColorJump|GoFileManager|GoLocker'
target=target.split('|')
file1=input(r'请输入你要检查的文件完整路径名字:')
file1.strip('"')
resultStr=''
target_file=open(file1,encoding='utf-8')
dict_result={}


for i in target_file:
    resultStr+=i
# list1=tuple(list1)

# print(resultStr)

for i in target:
    dict_result.setdefault(i,resultStr.count(i))

print('统计结果如下:')
for i in dict_result.items():
    print(i)

input()