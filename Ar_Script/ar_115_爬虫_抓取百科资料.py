import urllib.request
import re
from bs4 import BeautifulSoup


def main():
    url = "file:///F:/%E5%9F%B9%E8%AE%AD/HTML+CSS+JS/DIV+CSS/913z.html#"

    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")  # 使用 Python 默认的解析器
    # print(soup)

    '正则表达式加上find_all生成一个soup对象，然后遍历这个对象'
    for each in soup.find_all(href=re.compile("item")):
        print(each)
        # print(each.text, "->", ''.join(["", each["href"]]))
        # 上边用 join() 不用 + 直接拼接，是因为 join() 被证明执行效率要高很多


if __name__ == "__main__":
    main()