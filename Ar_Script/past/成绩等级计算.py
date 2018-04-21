tmp=input("请输入你的成绩：")
while not tmp.isdigit():
    tmp=input('你的输入有误!请重新输入：')
score=int(tmp)
if 60<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
elif 0<=score<60:
    print("F")
elif 80<=score<90:
    print("B")
elif 90<=score<=100:
    print("A")
else:
     print('非法成绩')