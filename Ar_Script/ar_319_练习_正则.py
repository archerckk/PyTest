#encoding=utf-8
import re

"""
1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'

用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"

2 字符串："one1two2three3four4" 用正则处理，输出 "1234"

3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。

4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。
"""

#1 已知字符串:info = '<a href="http://www.baidu.com">baidu</a>'

#用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"

info='<a href="http://www.baidu.com">baidu</a>'
reg_url=re.compile(r'.*"(.+)".+')
reg_title=re.compile(r'.+>(\w+).+')
url=reg_url.match(info).group(1)
title=reg_title.match(info).group(1)

assert url=='http://www.baidu.com'
assert title=='baidu'

#2 字符串："one1two2three3four4" 用正则处理，输出 "1234"
test2='one1two2three3four4'
reg_number=re.compile('\d')
result=reg_number.findall(test2)
print(''.join(result))


#3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。
text = "JGood is a handsome boy, he is cool, clever, and so on..."
reg_oo=re.compile(r'\w*o{2}\w*')
result_oo=reg_oo.findall(text)
print(result_oo)

#4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。
"""
要加引号的是因为有转义，不用加引号的是可以直接识别不用加引号
"""



"""
已知字符串：

info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'

要求完成下面2个小功能：
1.1 关闭[img]标签
1.2 将url()中的["]转为[']

最后结果字符串：

"test,&nbsp;url('http://www.baidu.com')&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com"></img>ininnnin<img src="http://www.dd.com"></img>"
"""

test3='test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'

reg_close=re.compile('dd.com">')
reg_yinhao=re.compile("'")
test3=re.sub(reg_close,'dd.com"></img>',test3)
test3=re.sub(reg_yinhao,'"',test3)
# print(re.match(reg_close,test3).group(1))
print(test3)