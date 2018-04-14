tmp=input('请输入一个年份(如：2017)：')
while not tmp.isdigit():
    tmp=input('你的输入有误！请重新输入：')
year=int(tmp)
if (year%4==0 and year%100!=0)or (year%400==0):
    print('%d是闰年'%year)
else:
    print('%d不是闰年'%year)