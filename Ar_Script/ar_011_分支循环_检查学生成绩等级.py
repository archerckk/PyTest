#0 一个班的成绩一般服从正态分布，也就是说平均成绩一般集中在70~80分之间，
# 因此根据统计规律，改下代码还是可以提高效率的。
score=input('请输入你的成绩：')
while not score.isdigit():
    print('你输入的字符不是数字！请重新输入：',end='')
    score=input()
score=int(score)

if 70<=score<80:
    print('你的成绩为：C')
elif 60<=score<70:
    print('你的成绩为：D')
elif 80<=score<90:
    print('你的成绩为：B')
elif score<60:
    print('你的成绩为：F')
elif 90<=score<=100:
    print('你的成绩为：A')
else:
    print('非法成绩')
