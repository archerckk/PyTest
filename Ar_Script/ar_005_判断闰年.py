#判断一个年份是不是润年，能被4整除，并且不被100整除，或者能被400整除
year=input('请输入你要查询的年份：')
while not year.isdigit():
    print('你输入的不是一个有效的年份!请重新输入：',end='')
    year=input()
year=int(year)
if (year%4==0 and year%100!=0) or year%400==0:
    print(str(year)+'是闰年！！！')
else:
    print(str(year)+'不是闰年！！！')
