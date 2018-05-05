import urllib.request
import chardet
import io

'打开一个网站并且获取网站的编码方式'

# '没有实现的目的'
# def findEncode():
#     # url=input('请输入你要检测的地址：')
#     url='http://www.fishc.com'
#     response=r.urlopen(url)
#     # print(type(response))
#     targetline=''
#     for i in response:
#         if io.BytesIO('charset') in response.readline():
#             targetline=i
#             break
#
#     (begin,end)=targetline.split('=')
#     end=end.strip('>')
#     return  end
#
#
#     # html=response.readline()
#     # html=html.decode('utf-8')
#     #
#     # print(html)
#
# print(findEncode())

'参考答案'

def main():
    url = 'http://www.fishc.com'

    response = urllib.request.urlopen(url)
    html = response.read()

    # 识别网页编码
    encode = chardet.detect(html)['encoding']
    if encode == 'GB2312':
        encode = 'GBK'

    print("该网页使用的编码是：%s" % encode)


if __name__ == "__main__":
    main()