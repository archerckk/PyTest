import urllib.request
import os


# def urlOpen(url):
#     '新建请求，打开网页，返回网页内容'
#     req=urllib.request.Request(url)
#     req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
#     response=urllib.request.urlopen(req)
#     html=response.read()
#
#     return html
#
# def get_page(url):
#     html=urlOpen(url).decode('utf-8')
#     a=html.find('current-comment-page')+23
#     b=html.find(']',a)
#     return html[a:b]
#
#
# def find_imgs(url):
#     html = urlOpen(url).decode('utf-8')
#     img_addrs = []
#
#     a = html.find('img src=')
#
#     while a != -1:
#         b = html.find('.jpg', a, a+255)
#         if b != -1:
#             img_addrs.append(html[a+9:b+4])
#             print(html[a+9:b+4])
#         else:
#             b = a + 9
#
#         a = html.find('img src=', b)
#
#     return img_addrs
#
# def save_img(folder,img_addrs):
#     for i in img_addrs:
#         filename=i.split('/')[-1]
#         with open(filename,'wb')as f:
#             img=urlOpen(i)
#             f.write(img)
#
# def downMeiMei(folder='OOXX',page=10):
#     os.mkdir(folder)
#     os.chdir(folder)
#
#     url='http://jandan.net/ooxx/'
#     page_num=int(get_page(url))
#     # print(page_num)
#     for i in range(page):
#         page_num-=1
#         page_url=url+'page-'+str(page_num)+'#comments'
#         img_addr_list=find_imgs(page_url)
#         print(img_addr_list)
#         save_img(folder,img_addr_list)
#
#
#
# downMeiMei(page=10)


import urllib.request
import os
import random



def get_Proxy(filename):
    Proxy_list=[]
    with open(filename)as f:
        for i in f:
            Proxy_list.append(i)
    return Proxy_list


def url_open(url):
    filename=r'C:\Users\chenzhibin\PycharmProjects\pytest\Ar_Script\result\ip_proxy.txt'

    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')

    proxies =get_Proxy(filename)
    proxy = random.choice(proxies)

    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=', b)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_mm(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
