import requests

url='http://advonline.goforandroid.com/adv_online/onlineadv HTTP/1.1'
User_Agent='Apache-HttpClient/UNAVAILABLE (java 1.4)'
access_key='3VX5LRSDBKSPFWF78MQ9DOL83ZUBFIO0'
prodKey='7G59NTHN7UBHXSSXI4QCMN35'
phead={
    "channel":"9135",
    "vcode":1004,
    "vname":"3.09",
    "country":"TW",
    "lang":"zh",
    "goid":"15415441001914d82658febbbc508",
    "aid":"4d82658febbbc508",
    "imei":"9010666766926998050",
    "imsi":"000",
    "sys":"7.0",
    "sdk":24,
    "net":"wifi",
    "hasmarket":1,
    "dpi":"480",
    "resolution":"1080*1812",
    "adid":"6b44a149-7c2c-4c9c-9fe0-007bfbf751c2",
    "ua":"Mozilla\/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build\/HUAWEINXT-AL10; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/65.0.3325.109 Mobile Safari\/537.36",
    "advposid":"2048"}

headers={
    'User_Agent':User_Agent,
}
form={
    'accessKey':access_key,
    'prodKey':prodKey,
    'phead':phead
}

request=requests.get(url=url,headers=headers,data=form)

print(request.status_code)