import requests
import bs4


def url_open(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    url = 'https://qingyuan.anjuke.com/sale/?kw=时代倾城&from=xlts_rm'
    res = requests.get(url=url, headers=headers)

    return res


with open('result/安居客.txt', 'r', encoding='utf-8')as f:
    soup=bs4.BeautifulSoup(f.read(),'html.parser')

    '标题信息筛选'
    title=[]
    targets=soup.find_all('div',class_='house-title')
    for i in targets:
        title.append(i.a.text.strip())

    '总价信息'
    total=[]
    targets=soup.find_all('span',class_='price-det')
    for i in targets:
        total.append(i.text)

    '单价信息'
    price=[]
    targets=soup.find_all('span',class_='unit-price')
    for i in targets:
        price.append(i.text)

    '详细信息'
    detail=[]
    targets=soup.find_all('div',class_='details-item')
    for i in targets:
        print(i.span.text)

        try:
            if i.span['class']=='brokername':
                print(i)
        except:
            continue
        # print(i.text)
