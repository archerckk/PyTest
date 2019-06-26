from bs4 import BeautifulSoup
import asyncio
import aiohttp
import time
import functools
#
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
#
#
# async def fetch_content(url):
#     async with aiohttp.ClientSession(
#         connector=aiohttp.TCPConnector(ssl=False)
#     ) as session:
#         async with session.get(url) as response:
#             return await response.text()
# @timeCounter
# async def main():
#     url = "https://movie.douban.com/cinema/later/beijing/"
#     init_page = await fetch_content(url)
#     init_soup = BeautifulSoup(init_page)
#
#     movie_names, urls_to_fetch, movie_dates = [], [], []
#
#     all_movies = init_soup.find('div', id="showing-soon")
#     for each_movie in all_movies.find_all('div', class_="item"):
#         all_a_tag = each_movie.find_all('a')
#         all_li_tag = each_movie.find_all('li')
#
#         movie_names.append(all_a_tag[1].text)
#         urls_to_fetch.append(all_a_tag[1]['href'])
#         movie_dates.append(all_li_tag[0].text)
#
#     tasks = [fetch_content(url) for url in urls_to_fetch]
#     pages = await asyncio.gather(*tasks)
#
#     for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
#         soup_item = BeautifulSoup(page)
#         img_tag = soup_item.find('img')
#
#         print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))
#
# asyncio.run(main())




#test write
async def getUrl(url):
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url)as connect:
            return await connect.text()
@timeCounter
async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    page_content=await getUrl(url)
    soup=BeautifulSoup(page_content,"html.parser")

    movieNames,movieImgs,movieTimes=[],[],[]

    allMovies=soup.find('div', id="showing-soon")

    for each_movie in allMovies.find_all('div',class_='item'):
        all_A_item=each_movie.find_all('a')
        all_li_item=each_movie.find_all('li')

        movieNames.append(all_A_item[1].text)
        movieTimes.append(all_li_item[0].text)
        movieImgs.append(all_A_item[1]['href'])

    tasks=[getUrl(each_img)for each_img in movieImgs]
    pages=await asyncio.gather(*tasks)

    for movie,movieTime,page in zip(movieNames,movieTimes,pages):
        imgSoup=BeautifulSoup(page,"html.parser")
        img_tag=imgSoup.find('img')

        print('{} {} {}'.format(movie,movieTime,img_tag['src']))

asyncio.run(main())