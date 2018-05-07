from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

def test_result(soup):
    result=soup.find(text=re.compile('百度百科尚未收录词条'))
    if result:
        print(result[0:-1])
        return False
    else:
        return True

def summary(soup):
    word = soup.h1.text
    # 如果存在副标题，一起打印
    if soup.h2:
        word += soup.h2.text
    # 打印标题
    print(word)
    # 打印简介
    if soup.find(class_="lemma-summary"):
        print(soup.find(class_="lemma-summary").text)
        print('-'*200)
    return word

def get_url(soup):
    for each in soup.find_all(href=re.compile('view')):
        content = ''.join([each.text])
        url2 = ''.join(['http://baike.baidu.com', each['href']])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        # if soup2.find(class_='lemma-summary'):
        #     print(soup2.find(class_='lemma-summary').text)
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, '-->', url2])
        yield content


def getLink():
    head = {}
    head['User-Agetn'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
    word = input('请输入你要查找的关键字：')
    keyword = urllib.parse.urlencode({'word': word})
    url = 'https://baike.baidu.com/search/word?%s' % keyword
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    if test_result(soup):
        summary(soup)
    #
        print('以下是相关链接：')
        each=get_url(soup)

        while True:
            for  i in range(10):
                try:
                    print(next(each))
                    print('-'*200)
                except StopAsyncIteration:
                    break
            command=input('\n请输入任意字符继续(q退出)：')
            if command!='q':
                continue
            else:
                break
getLink()
# if __name__ == '__main__':
#     getLink()

