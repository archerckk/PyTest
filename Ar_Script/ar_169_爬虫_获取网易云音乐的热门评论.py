import requests
import json


def urlopen(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
               'Referer': 'https://music.163.com'
               }

    encSecKey = 'cd49dc98c0388244c3d10f97a50fcae0f16cc2a56c03780e302d97bff7f094c07a6f6967bca4459e5a9d01af65f4313b13052704b6add9b29b3fc11a42dce986eee4c0aa8ee2c9c2017232a150aa53df273a932b358e55106498fe90979102918d086d72696806f9f5704a20c19280cb598ae11983e89397e3f61e0d6745f0e4'
    params = 'IWvv4bxkO0aMJn48PPjranphtvWQCAGQItbVkHRUWv6scTcM9v4YO01iLCx34cjFztsXq0sBVeCadAanHy+Z3Rc1ILxToJ2AomN3w1AOBCliPPnDimXyRuBiWhtb93h2vsCaKZHwa49VyhKS48rcz3FWnkhF6TlRszvQQjqOYAyL7m8pZwWxEdg5GoXH7W8m'
    data = {'encSecKey': encSecKey, 'params': params}

    name_id = url.split('=')[1]
    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)

    res = requests.post(target_url, headers=headers, data=data)

    return res


def get_hot_content(res):
    result_json = json.loads(res.text)
    hot_comments_list = result_json['hotComments']
    # for i in hot_comments_list:
    #     print(i['user'])

    with open('result/网易云音乐2.txt', 'w', encoding='utf-8')as f:
        for i in hot_comments_list:
            f.write(i['user']['nickname']+ '：\n\n')
            f.write(i['content'] + '\n')
            f.write('--' * 60+'\n')


def main():
    host = 'https://music.163.com/#/song?id=27808044'
    # host=input('请输入你要查找的网站：')
    res = urlopen(host)
    get_hot_content(res)


if __name__ == '__main__':
    main()
