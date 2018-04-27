str1='''
{"uid":"3062659467949056474","hasmarket":1,"sbuy":0,"sys":"4.4.4","imei":"3062659467949056474","resolution":"720*1184","aid":"e9d1eba1fe333af9","net":"wifi","pkgs":"net.openvpn.openvpn,com.scan.traceroute,com.instagram.android,com.facebook.katana,com.vklancer.savespikes,com.voyagephotolab.picframe,com.google.android.gms.drive.sample.demo,sightidea.com.setlocale,com.sohu.inputmethod.sogou,com.twitter.android,com.speedsoftware.rootexplorer,","cid":"212","lang":"en","vname":"1.0","pversion":21,"country":"US","adid":"9c085d08-f260-4747-aebc-305f95be6c5e","advposid":"3571","ua":"Mozilla\/5.0 (Linux; Android 4.4.4; HTC D820t Build\/KTU84P) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/33.0.0.0 Mobile Safari\/537.36","dpi":"320","sdk":19,"imsi":"000","channel":"101","goid":"1500118235188e9d1eba1fe333af9","vcode":1}

'''
target=['IMEI','imei','IMSI','imsi','email']

tmp=str1.split(',')
result={}
for i in tmp:
   try:
    (begin,end)=i.split(":")
    if begin in target:
        result.setdefault(begin,end)
   except ValueError:
       pass
for i in result:
    print(i,result[i])
