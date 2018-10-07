from time import ctime,sleep
import threading
from selenium import webdriver


def test_baidu(browser,keyword):
    print('start:%s %s'%(browser,ctime()))

    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='ie':
        driver=webdriver.Ie()
    elif browser=='ff':
        driver=webdriver.Firefox()
    else:
        print('传输传入有误!!!')

    driver.get('http://www.baidu.com')

    driver.find_element_by_id('kw').send_keys(keyword)
    driver.find_element_by_id('su').click()
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    threads=[]

    key_dict={'chrome':'谷歌搜索','ie':'IE搜索','ff':'火狐搜索'}

    file_length=range(len(key_dict))

    for browser,keyword in key_dict.items():
        t=threading.Thread(target=test_baidu,args=(browser,keyword))
        threads.append(t)

    for file in file_length:
        threads[file].start()

    for file in file_length:
        threads[file].join()

    print('All end:%s'%(ctime()))