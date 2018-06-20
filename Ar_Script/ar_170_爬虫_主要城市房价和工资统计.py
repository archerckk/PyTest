import requests
import openpyxl
import re
import bs4


def url_open(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    res=requests.get(url,headers=headers)

    return res

def find_data(res):
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    content=soup.find(id="Cnt-Main-Article-QQ")
    city_contend=iter(content.find_all("p", style="TEXT-INDENT: 2em"))

    data=[]
    for i in city_contend:
        if i.text.isnumeric():
            data.append([
                re.search(r'\[(.*)\]',next(city_contend).text).group(1),
                re.search(r'\d.*', next(city_contend).text).group(),
                re.search(r'\d.*', next(city_contend).text).group(),
                re.search(r'\d.*', next(city_contend).text).group()
            ])
    return data

def output_exl(data):
    wb=openpyxl.Workbook()
    wb.guess_type=True
    ws=wb.active
    ws.append(['城市','房价','工资','房价工资比'])

    for i in data:
        ws.append(i)

    wb.save('result/2017全国城市房价 工资排行榜.xlsx')

#id: "Cnt-Main-Article-QQ"


def main():
    host='http://news.house.qq.com/a/20170702/003985.htm'
    res=url_open(host)
    data=find_data(res)
    output_exl(data)


if __name__ == '__main__':
    main()