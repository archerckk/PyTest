import requests

def urlopen(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    payload={'q':'零基础入门学python','sort':'sale-desc'}
    res=requests.get(url,headers=headers,params=payload)

    return res


def main():
    host='https://s.taobao.com/search'
    res=urlopen(host)

    with open('resources/taobao.txt','w',encoding='utf-8')as f:
        f.write(res.text)



if __name__ == '__main__':
    main()
