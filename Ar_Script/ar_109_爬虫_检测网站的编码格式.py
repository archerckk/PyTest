import urllib.request as r
import io
def findEncode():
    # url=input('请输入你要检测的地址：')
    url='http://www.fishc.com'
    response=r.urlopen(url)
    # print(type(response))
    targetline=''
    for i in response:
        if io.BytesIO('charset') in response.readline():
            targetline=i
            break

    (begin,end)=targetline.split('=')
    end=end.strip('>')
    return  end


    # html=response.readline()
    # html=html.decode('utf-8')
    #
    # print(html)

print(findEncode())