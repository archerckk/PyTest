import re
import requests
import json

def url_open(url,keyword):
    headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    payloads={'q':keyword,'sort':'sale-desc'}

    res=requests.get(url,headers=headers,params=payloads)

    return res


def get_items(res):
    g_page_config=re.search(r'g_page_config = (.*?);\n',res.text)
    page_config_json=json.loads(g_page_config.group(1))
    page_items = page_config_json['mods']['itemlist']['data']['auctions']

    results=[]
    for each_item in page_items:
        dict1 = dict.fromkeys(('nid', 'title', 'detail_url', 'view_price', 'view_sales', 'nick'))
        dict1['nid'] = each_item['nid']
        dict1['title'] = each_item['title']
        dict1['detail_url'] = each_item['detail_url']
        dict1['view_price'] = each_item['view_price']
        dict1['view_sales'] = each_item['view_sales']
        dict1['nick'] = each_item['nick']
        results.append(dict1)

    return results


def cal(items):
    sales=0

    for i in items:
        if '小甲鱼' in i['title']:
            sales+=(int(re.search(r'\d+',i['view_sales']).group()))

    return sales



def main():
    length=3
    total=0

    host="https://s.taobao.com/search"
    keyword=input('请输入你要查找的宝贝：')

    res=url_open(host,keyword)
    items=get_items(res)
    sales=cal(items)
    print(sales)




if __name__ == '__main__':
    main()