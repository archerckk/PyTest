import re

"""
1、少于三位的数字是可以匹配的
2、多于3位数字产生逗号
3、不会匹配不，号不是出现在第三位后面的
4、不会匹配多于3位不会产生逗号的
"""

# regex=re.compile(r"((\d*,+\d{3})+)?|\d{1,3}")
# result=regex.search('1234')
# print(result.group())


"""
1、姓氏和名字都是一个首字母大写的单词
2、中间有一个空格
3、不匹配非单词字符
4、不匹配首字母没有大写，没有名字，没有姓氏的单词
"""
# regex=re.compile(r"([A-Z][a-zA-Z]+ )([A-Z][A-Za-z]+)")
# result=regex.search('Abc ABD')
# print(result)


"""
1、第一个单词是Alice、Bob、Carol中的一个
2、第二个单词是eats、pets、throws中的一个
3、第三个单词是apples、cats、baseballs中的一个
4、表达式不区分大小写
"""
regex=re.compile(r"(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.",re.I)
result=regex.search('Alice eats apples.')
result2=regex.search('Bob pets cats.')
result3=regex.search('Carol throws baseballs.')
result4=regex.search('AlicE throws 7 baseballs.')
print(result)
print(result4)