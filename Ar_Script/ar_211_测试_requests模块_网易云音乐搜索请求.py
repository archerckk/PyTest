import requests

test_url='http://music.163.com/weapi/search/suggest/web?csrf_token='

#https测试链接
test_url2='https://www.zhihu.com/'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'}
form={
'params': 'da9C6vME6zCNsek6T07Jyy/vhbuE6jqXcReHKTL9xZa1sYygUx2ezdbFITgHLc8kfwHUcPuYXL3JitHcO3+NFHELEM+0fnHDKCDXz1uNU71vUKHUajkX+TS0q4m1j2P',
'encSecKey': '9f4f282a5ee79c4450cf32b39ed10ce545f8adbdd67120dfbc96b3b6539034a954c8367f78307bc24f66e3cf732e93a10b5eeadf798a6587ebdebe2198dad8a9a8422f8f66eb6b66376968430a1afc4b9a97578deee01e1de7339d4e4b1b1525dbe8ae6c8dc799748f0e7078079268f5aa3b744099e5ceeb189841a133d4d8e7'
}

#这是一个post表单的请求
# reponse=requests.get(test_url,headers=headers,data=form)

#这是一个https的请求
reponse=requests.get(test_url2,headers=headers)
print(reponse.status_code)
print(reponse.headers)
print(reponse.text)


'''
当遇到一些特有的证书不在certifi包中，这时候就需要先通过浏览器找到需要的证书名称，然后通过浏览器设置中的证书选项导出对应的证书和秘钥，
加上一个cert参数指定证书和秘钥的路径就可以了
requests.post(url,cert=('/path/client.cert','path/client.key'))
'''