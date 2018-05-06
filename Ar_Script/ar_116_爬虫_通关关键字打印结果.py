# from bs4 import BeautifulSoup as bs
# import urllib.request
# import re
# import urllib.parse
#
# def main():
#     # keyword=input('请输入你要查找的内容：')
#     keyword='西游记'
#     keyword=urllib.parse.urlencode({'word':keyword})
#     head={}
#     head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
#     url="http://baike.baidu.com/search/word?%s" % keyword
#     print(url)
#     req=urllib.request.Request(url,headers=head)
#     print(req.get_full_url())
#     # response=urllib.request.urlopen(req)
#     # print(response.geturl())
#     # content=response.read()
#     # print(content)
#     # soup=bs(content,'html.parser')
#     #
#     # for each in soup.find_all(href=re.compile('view')):
#     #     print(each.text,'-->',''.join(['http://baike.baidu.com',each['href']]))
#
# if __name__ == '__main__':
#     main()
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

def main():
    keyword = input("请输入关键词：")
    keyword = urllib.parse.urlencode({"word":keyword})
    response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    for each in soup.find_all(href=re.compile("view")):
        content = ''.join([each.text])
        url2 = ''.join(["http://baike.baidu.com", each["href"]])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, " -> ", url2])
        print(content)

if __name__ == "__main__":
    main()