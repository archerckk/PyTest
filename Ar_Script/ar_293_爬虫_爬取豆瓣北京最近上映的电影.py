from bs4 import BeautifulSoup
import requests
import time
import functools

def timeCounter(func):
    @functools.wraps(func)
    def warper(*args,**kwargs):
        start=time.perf_counter()
        res=func()
        end=time.perf_counter()
        result=end-start
        print("{}执行了{}秒".format(func.__name__,result))
        return res
    return warper

@timeCounter
def main():
    url='https://movie.douban.com/cinema/later/beijing/'
    content=requests.get(url).content
    bfObject=BeautifulSoup(content)
    allMovies=bfObject.find('div',id='showing-soon')

    for eachMovie in allMovies.find_all('div',class_='item'):
        all_a_Tag=eachMovie.find_all('a')

        all_li_tag=eachMovie.find_all('li')

        movieName=all_a_Tag[1].text
        imgTarget = all_a_Tag[1]["href"]
        movieTime=all_li_tag[0].text

        responseBody=requests.get(imgTarget).content
        bfImgObject=BeautifulSoup(responseBody)
        imgResult=bfImgObject.find('img')

        print('{} {} {}'.format(movieName,movieTime,imgResult["src"]))


main()
