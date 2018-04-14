#编写程序：要求用户输入1到100之间的数字并判断，输入符合要求并打印“你妹好漂亮”
#不符合要求打印“你弟好丑”

number=input('请输入1-100之间的数字：')
number=int(number)
if 1<=number<=100:
    print('你妹好漂亮哦')
else:
    print('你弟好丑哦')

