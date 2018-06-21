import requests
from bs4 import BeautifulSoup as bs
import openpyxl

def url_open(url):
    header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

    res=requests.get(url,header)

    return res


def find_movies(res):
    soup = bs(res.text, 'html.parser')

    '电影名'
    movies=[]
    targets=soup.find_all('div',class_='hd')
    for i in targets:
        movies.append(i.a.span.text+'  ')


    '评分'
    score=[]
    targets = soup.find_all('span', class_='rating_num')
    for i in targets:
        #txt执行代码
        # score.append('评分：%s  '%i.text)
        'excel执行代码'
        score.append(i.text)


    '电影介绍'
    info=[]
    targets=soup.find_all('div',class_='bd')
    for i in targets:
        try:
            info.append(i.p.text.split('\n')[1].strip()+i.p.text.split('\n')[2].strip())
        except:
            continue


    '显示结果'
    result=[]
    length=len(movies)
    for  i in range(length):
        # 'txt执行代码'
        # result.append(movies[i]+score[i]+info[i]+'\n')
        'excel执行代码'
        result.append([movies[i],score[i],info[i]])


    return result




def find_depth(res):
    soup = bs(res.text, 'html.parser')
    depth=soup.find('span',class_='next').previous_sibling.previous_sibling.text

    return int(depth)


def save_excel(result):
    wb=openpyxl.Workbook()
    ws=wb.active
    ws.append(['电影名','评分','电影介绍'])

    for i in result:
        ws.append(i)

    wb.save('result/豆瓣top250.xlsx')



def main():
    host='https://movie.douban.com/top250'
    res=url_open(host)

    '获取一个要爬取的页面总数'
    depth=find_depth(res)

    result=[]
    for i in range(depth):
        url=host+'?start=%d&filter='%(25*i)
        res=url_open(url)
        result.extend(find_movies(res))

    # 'txt执行代码'
    # with open('result/douban.txt','w',encoding='utf-8')as f:
    #     f.writelines(result)

    'excel执行代码'
    save_excel(result)



if __name__ == '__main__':
    main()