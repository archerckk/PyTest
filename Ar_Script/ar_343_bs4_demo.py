# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re

with open('bs4.html',encoding='utf-8')as f:
    response=f.read()

soup=BeautifulSoup(response,'html.parser')

div=soup.find_all('span',attrs={'style':re.compile(r'background:(FB9252)|(59A5EB)|(B199FF)|(FB9252);')})

for i in div:
    print(i.text)