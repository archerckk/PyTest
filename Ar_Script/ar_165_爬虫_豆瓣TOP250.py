import requests
from bs4 import BeautifulSoup as bs
import openpyxl
from openpyxl.styles import NamedStyle,Alignment,Font,PatternFill
from openpyxl.styles.colors import RED


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
    wb.guess_type=True
    ws=wb.active


    '标题样式'
    title_style=NamedStyle(name='title_style')
    title_style.alignment=Alignment(horizontal='center',vertical='center')
    title_style.font=Font(size=14,bold=True)
    title_style.fill=PatternFill(fill_type='solid',fgColor='b2b2b2')


    '内容样式'
    content_style = NamedStyle(name='content_style')
    content_style.alignment = Alignment(horizontal='center', vertical='center')
    content_style.font = Font(size=12)

    '注册标题和内容样式'
    wb.add_named_style(title_style)
    wb.add_named_style(content_style)

    ws.append(['电影名','评分','电影介绍'])
    for i in ws.rows:

        ws[i[0].coordinate].style=title_style
        ws.column_dimensions['A'].width=20
        ws[i[1].coordinate].style = title_style
        ws.column_dimensions['B'].width = 20
        ws[i[2].coordinate].style = title_style
        ws.column_dimensions['C'].width = 150


    for i in result:
        ws.append(i)


    for i in ws.iter_rows(min_row=2,min_col=1,max_row=251,max_col=3):
        ws[i[0].coordinate].style=content_style
        ws.column_dimensions['A'].width = 20
        # ws[i[1].coordinate].number_format = '[>9.5][RED]#.0分'
        ws[i[1].coordinate].style = content_style
        ws.column_dimensions['B'].width = 20
        ws[i[2].coordinate].style = content_style
        ws.column_dimensions['C'].width = 150




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