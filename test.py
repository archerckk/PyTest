import os
import time
# import test2
# def cd():
#     print('x')
# if __name__ =='__main__':
#     test2.ab()

# '''查找包括子文件夹在内的目标文件，并写入TXT文档保存'''
#
# def find_video(fileName,target):
#     os.chdir(fileName)
#     allFile=os.listdir(os.curdir)
#     for i in allFile:
#         ext=os.path.splitext(i)[1]
#         if ext in target:
#             fileList.append(os.getcwd()+os.sep+i+os.linesep)
#         if os.path.isdir(i):
#             find_video(i,target)
#             os.chdir(os.pardir)
#
#
# fileName=input('请输入带查找的初始目录：')
# program_dir=os.getcwd()
# fileList=[]
# target=['.avi','.rm','.mp4','.rmvb','.wmv']
# find_video(fileName,target)
# f=open(program_dir+os.sep+'video_list.txt','w',encoding='utf-8')
# f.writelines(fileList)
# f.close()

# '''插件化例子'''
#
# class Plauin(object):
#     def __init__(self):
#         self.export_methods=[]
#
#     def plauin(self,owner):
#         for i in self.export_methods:
#             owner.__dict__[i.__name__]=i
#     def plauout(self,owner):
#         for i in self.export_methods:
#            del owner.__dict__[i.__name__]
#
# class Feature(Plauin):
#     def __init__(self):
#         super(Feature,self).__init__()
#         self.export_methods.append(self.get_value)
#
#     def get_value(self):
#         print('This is a feature')
#
# class Test:pass
#
# test=Test()
# Feature().plauin(test)
# test.get_value()

# '''property的练习'''
# class Test:
#     def __init__(self):
#         self.show='这是初始值'
#
#     def getx(self):
#         return self.show
#
#     def setx(self,value):
#         self.show=value
#
#     def delx(self):
#         del self.show
#
#     x=property(getx,setx,delx,'这是一个property测试')
#
# test=Test()
# test.setx('这是修改值')
# print(test.x)


# '''修饰属性的练习'''
#
# class Test1(object):
#     def __init__(self,func):
#         self.x=func
#
#     def __call__(self):
#         print('这是第一次打印')
#         self.x()
#
#
# @Test1
# def fuc():
#     print('这是修饰属性调用')
#
#
# fuc()

# class Hello(object):
#
#     pass
#
#
#     @classmethod
#     def print_hello(cls):
#         print("Hello")
#
# Hello.print_hello()


#
# '''staticmethod修饰符的测试'''
#
# class Pizza(object):
#     @staticmethod
#     def test1(x,y):
#         return x+y
#     def test2(self):
#         return self.test1
#
# class Pizza2(Pizza):
#     def tes1(self):
#         print('这是子类重构的方法')
#
#     def test2(self):
#         x=2
#         y=2
#         return Pizza2.test1(x,y)
#
#
# p=Pizza2()
# print(p.test1(1,1))
# print(p.test2())
# p.tes1()


# class Nint(int):
#     def __new__(cls, arg=0):
#         if isinstance(arg, str):
#             total = 0
#             for each in arg:
#                 total += ord(each)
#             arg = total
#         return int.__new__(cls, arg)
#     def __setattr__(self, key, value):
#         self.key=value+1

# class Test:
#     def __getattr__(self, item):
#         print('你访问的属性不存在！！')
#
# t=Test()
# t.x
#
# class MyProperty:
#     def __init__(self, fget=None, fset=None, fdel=None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#
#     def __set__(self, instance, value):
#         self.fset(instance, value)
#
#     def __delete__(self, instance):
#         self.fdel(instance)
#
#
# class C:
#     def __init__(self):
#         self._x = None
#
#     def getX(self):
#         return self._x
#
#     def setX(self, value):
#         self._x = value
#
#     def delX(self):
#         del self._x
#
#     x = MyProperty(getX, setX, delX)

#
# class MyProperty:
#     def __init__(self,getx=None,setx=None,delx=None):
#         self.getx=getx
#         self.setx=setx
#         self.delx=delx
#
#     def __get__(self, instance, owner):
#         return self.getx(instance)
#
#     def __set__(self, instance, value):
#         self.setx(instance,value)
#
#     def __delete__(self, instance):
#         self.delx(instance)
#
# class C:
#     def __init__(self):
#         self._x=None
#
#     def getx(self):
#         return  self._x
#
#     def setx(self,value):
#         self._x=value
#
#     def delx(self):
#         del self._x
#
#     x=property(getx,setx,delx)
#
# c=C()

# class Celsius:
#     def __init__(self,value=26):
#         self.value=float(value)
#
#     def __get__(self, instance, owner):
#         return self.value
#
#     def __set__(self, instance, value):
#         self.value=value
#
# class Fahrenheit:
#     def __get__(self, instance, owner):
#         return instance.cel*1.8+32
#
#     def __set__(self, instance, value):
#         instance.cel=(value-32)/1.8
#
# class Tempature:
#     cel=Celsius()
#     fah=Fahrenheit()

# #复习文件处理练习1
# def savefile_w(filename):
#     f=open(filename,'w')
#     print('请输入你要输入的内容（输入<：w>保存）：\n')
#     while True:
#         content=input()
#         if content!=':w':
#             f.write('%s\n'%content)
#         else:
#             break
#     f.close()
# filename=input('请输入你的文件名：')
# savefile_w(filename)

#复习文件处理练习2
#
# def compareFile(file1,file2):
#     f1=open(file1)
#     f2=open(file2)
#     differ=[]
#     line_count=0
#
#     for i in f1:
#         line_count+=1
#         if i!=f2.readline():
#             differ.append(line_count)
#
#     if len(differ)==0:
#         print('两个文件完全一样')
#     else:
#         print('两个文件共有%d处不同:'%len(differ))
#         for i in differ:
#             print('第%d行不一样'%i)
#
#
# file1=input('请输入第一个文件的名字：')
# file2=input('请输入第二个文件的名字：')
#
# compareFile(file1,file2)

#复习文件替换练习
# def replace(filename,keyWord,newWord):
#     f=open(filename,encoding='utf-8')
#     count=0
#     content=[]
#
#     for i in f:
#         if keyWord in i:
#             count+=i.count(keyWord)
#             i=i.replace(keyWord,newWord)
#         content.append(i)
#
#     print('文件%s中共有%d个【%s】'%(filename,count,keyWord))
#     print('你确定把所有的【%s】替换成【%s】嘛？\n【YES/NO】：'%(keyWord,newWord),end='')
#     j=input()
#     f = open(filename, 'w', encoding='utf-8')
#     if j=='YES':
#         f.writelines(content)
#         f.close()
#     else:
#         f.close()
#         return None
#
# fileName=input('请输入你要替换内容的文件名：')
# keyWord=input('请输入你要查找的关键字：')
# newWord=input('请你输入你所要替代的内容：')
# replace(fileName,keyWord,newWord)

#复习文件模块_按文件类型统计文件个数
# def countFile():
#     filelist=os.listdir(os.curdir)
#     file_dict={}
#
#     for i in filelist:
#         if os.path.isdir(i):
#             file_dict.setdefault('文件夹',0)
#             file_dict['文件夹']+=1
#         else:
#             ext=os.path.splitext(i)[1]
#             file_dict.setdefault(ext,0)
#             file_dict[ext]+=1
#     for i in file_dict:
#         print('在当前目录下有【%s】%d个'%(i,file_dict[i]))
#
# countFile()

#复习统计当前文件夹下所有文件的文件大小
# def countSize():
#     filelist=os.listdir(os.curdir)
#     file_dict={}
#
#     for i in filelist:
#         if os.path.isdir(i):
#             pass
#         else:
#             file_dict.setdefault(i,os.path.getsize(i))
#
#     for i in file_dict.keys():
#         print('%s【%dBytes】'%(os.path.split(i)[1],file_dict[i]))
#
# countSize()


#复习文件模块_将改目录下的所有指定格式的文件写入一个txt文档保存
# def search_file(start_file,target):
#     allfile=os.listdir(start_file)
#
#     for i in allfile:
#         ext=os.path.splitext(i)[1]
#         if ext in target:
#             file_list.append(os.curdir+os.sep+i+os.linesep)
#
#         if os.path.isdir(i):
#             search_file(i,target)
#             os.chdir(os.pardir)
#
# start_file=os.curdir
# work_file=os.curdir
# target=['.py','.txt']
# file_list=[]
#
# search_file(start_file,target)
#
# f=open(work_file+os.sep+'file_list.txt','w',encoding='utf-8')
# f.writelines(file_list)
# f.close()

# print(os.getcwd())
#
#
# def search_file(start_file,target):
#     os.chdir(start_file)
#     allfile=os.listdir(os.curdir)
#
#     for i in allfile:
#         ext=os.path.splitext(i)[1]
#         if ext in target:
#             filelist.append(os.getcwd()+os.sep+i+os.linesep)
#         if os.path.isdir(i):
#             search_file(i,target)
#             os.chdir(os.pardir)
#
# filelist=[]
# target=['.py','.txt']
# start_file=os.getcwd()
# work_file=os.getcwd()
#
# search_file(start_file,target)
#
# f=open(work_file+os.sep+'file_record.txt','w',encoding='utf-8')
# f.writelines(filelist)
# f.close()

#复习查找文本里面对应的内容并且打印它所在的位置
# def pos_print(key_dict):
#     keys=key_dict.keys()
#     keys=sorted(keys)
#     for i in keys:
#         print('关键字出现在%d行，第%s个位置'%(i,str(key_dict[i])))
#
# def get_pos(line,key):
#     pos=[]
#
#     begin=line.find(key)
#     while begin!=-1:
#         pos.append(begin + 1)
#         begin=line.find(key,begin+1)
#     return pos
#
# def search_txt_file(filename,key):
#     f=open(filename,encoding='utf-8',errors='ignore')
#     count=0
#     key_dict={}
#     for i in f:
#         count+=1
#         if key in i:
#             pos=get_pos(i,key)
#             key_dict[count]=pos
#     return key_dict
#
# def search_all_file(key,detail):
#     allfile=os.walk(os.getcwd())
#     txt_file_list=[]
#
#     for i in allfile:
#         for each_file in i[2]:
#             ext=os.path.splitext(each_file)[1]
#             if ext=='.txt':
#                 each_file=os.path.join(i[0],each_file)
#                 txt_file_list.append(each_file)
#
#     for i in txt_file_list:
#         key_dict=search_txt_file(i,key)
#         if key_dict:
#             print('='*38)
#             print('在文件【%s】中，找到关键字【%s】'%(i,key))
#             if detail=='YES':
#                 pos_print(key_dict)
#
# key=input('请输入你要查找的关键字：')
# detail=input('你确定要打印么？【YES/NO】：')
# search_all_file(key,detail)

# class countItem:
#
#     def __init__(self,*args):
#         self.valus=[x for x in args]
#         self.count={}.fromkeys(range(len(self.valus)),0)
#
#     def __len__(self):
#         return len(self.valus)
#
#     def __getitem__(self, item):
#         self.count[item]+=1
#         return self.valus[item]

#0 编写程序 ，要求打印出“你好，姓名！”
# name=input('请输入你的姓名：')
# print('你好，'+name)

#编写程序：要求用户输入1到100之间的数字并判断，输入符合要求并打印“你妹好漂亮”
#不符合要求打印“你大爷好丑”
# number=int(input('请输入1-100之间的数字：'))
#
# if 1<=number<=100:
#     print('哎哟好帅')
# else:
#     print('哎哟好丑')

#字符串的输入数字的判断
# num=input('请输入一个数字：')
# while not num.isdigit():
#     print('你输入有误，请重新输入：',end='')
#     num=input()
#
# print('你输入的数字为：%d'%int(num))

#判断一个年份是不是闰年
# year=input('请输入一个年份：')
# while not year.isdigit():
#     print('输入有误！，请重新输入：',end='')
#     year=input()
# year=int(year)
# if (year%4==0 and year%100!=0)or year%400==0:
#     print(str(year)+'是闰年')
# else:
#     print(str(year)+'不是闰年not 1 or 0 or 3 and 4 or 5 and 6 or 7 and 8 and 9')

#%号怎么替代
# a=12
# b=10
# print(a-(a//b)*b)

#0 写一个程序打印出0~100所有的奇数
# a=0
# while a<=100:
#     if a%2!=0:
#         print(a,end=' ')
#     a+=1
# print()
# for a in range(101):
#     if a%2==0:
#         print(a,end=' ')

#爱因斯坦的阶梯
# i=0
# target=0
# judge=0
# for i in range(100):
#     if target%2==1 and target%3==2 and target%5==4 and target%6==5 and target%7==0:
#         judge=1
#     else:
#         target=i*7
#
# if judge==1:
#     print(target)
# else:
#     print('在该范围找不到')

# str4='123 \
#       456.'
# print(str4)

# psw=input('请输入需要检查的密码组合：')
# security_level=0
# judge_len=0
# judge_word=0
# zimu='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# fuhao=r'~!@#$%^&*()_+=-{}|\[]:";<>,.?'
# num='1234567890'
#
# if len(psw)<8:
#     judge_len=1
# elif 8<=len(psw)<16:
#     judge_len=2
# else:
#     judge_len=3
#
# for i in psw:
#     if i in zimu:
#         judge_word+=1
#         break
#
# for i in psw:
#     if i in num:
#         judge_word+=1
#         break
#
# for i in psw:
#     if i in fuhao:
#         judge_word+=1
#         break
#
# while 1:
#     if judge_len==1 or judge_word==1:
#         print('你的安全等级为：低')
#     elif judge_len==2 or judge_word==2:
#         print('你的安全等级为：中')
#     elif judge_len==3 or judge_word==3:
#         print('你的安全等级为：高\n请继续保持')
#         break
#
#     print('1.密码必须由数字、字母、特殊字符三种组合\n2.密码长度不能低与16位\n3.请以字母开头')
#     break


#
# psw=input('请输入你要检查的密码：')
# word_level=0
# len_level=0
# zimu=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C'
#       , 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
# shuzi='1234567890'
# fuhao='`~!@#$%^&*()-_+={}[]|\'\;:<>,./?"'
#
# for i in psw:
#     if i in zimu:
#         word_level+=1
#         break
#
# for i in psw:
#     if i in shuzi:
#         word_level+=1
#         break
#
# for i in psw:
#     if i in fuhao:
#         word_level+=1
#         break
#
# if len(psw)<8:
#     len_level=1
# elif 8<=len(psw)<16:
#     len_level=2
# elif len(psw)>16:
#     len_level=3
#
# while 1:
#     if word_level==1 or len_level==1:
#         print('你的密码安全等级为：低')
#     elif word_level==2 or len_level==2:
#         print('你的密码安全等级为：中')
#     elif (word_level==3 or len_level==3 )and not psw.startswith(zimu):
#         print('你的密码安全等级为：较高')
#         break
#     else:
#         print('你的密码安全等级为：高\n请继续保持！！')
#     print('1.密码必须由数字、字母、特殊字符三种组合\n2.密码长度不能低与16位\n3.请以字母开头')
#     break

#三元操作符练习
# x,y,z=5,7,6
#
# small=x if (x<y and x<z)else (y if y<z else z)

#密码输入检查脚本复习
# '''
# 1.输入*号的话密码输入的次数不计算
# 2.每输入错误一次，提示重新输入，并提示还剩下的次数
# 3.输入正确，提示可以进入程序
# 4.输入次数用完的话，提示程序锁定，并结束程序
# '''
#
#
# target='test'
# psw=input('请输入密码：')
# times=3
# while 1:
#     if '*'in psw:
#        print('你输入的密码不能包含“*”号，请重新输入：',end='')
#        psw=input()
#     else:
#         if psw!=target:
#             times-=1
#             print('你输入的密码错误！你还有%d次机会！请重新输入密码：'%times,end='')
#             psw=input()
#         if times<=1:
#             print('你的账户已锁定！程序结束！！')
#             break
#         if psw==target:
#             print('成功进入程序!')
#             break

#求1000以内的水仙花数,水仙花数其实是立方而不是平方
# for i in range(100,1000):
#     bai=i//100
#     shi=i%100//10
#     ge=i%100%10
#
#     if i==bai**3+shi**3+ge**3:
#         print(i)
#     else:
#         pass
#     i+=1

#计算三种颜色的球的组合337
# print('red\tgreen\tyellow')
# count=0
# for red in range(4):
#     for green in range (4):
#         for yellow in range(2,7):
#             if red+green+yellow==8:
#                 print(red,'\t',green,'\t\t',yellow,'\t')
#                 count+=1
# print(count)

#密码检查脚本

# target='test'
# # psw=input('请输入你的密码：')
# times=3
#
# while times:
#     psw = input('请输入你的密码：')
#     if psw==target:
#         print('成功登录！！')
#     elif '*' in psw:
#         print('你输入的密码不能包含"*"号，请重新输入：',end='')
#         # psw=input()
#     else:
#         print('你输入的密码不正确！！你还有%d次机会！！请重新输入：'%times,end='')
#         # psw=input()
#     times-=1


# password="test"
# times=3
# while times:
#     tmp = input("请输入你的密码:")
#     if password == tmp:
#         print("密码正确，进入程序……")
#         break
#     elif "*" in tmp:
#         print("你的输入不能包含'*'号！你还有" + str(times) + "机会", end="")
#         continue
#     else:
#         print("你的密码不正确!你还有" + str(times-1) + "机会", end="")
#     times-=1


# list2=[]
#
# for x in range(10):
#     for y in range(10):
#         if x %2==0 and y%2!=0:
#             list2.append((x,y))
#
# for i in list2:
#     print(i)

# list1=['1.Just do it','2.一切皆有可能','3.编程改变世界','4.Impossible is Nothing']
#
# list2=['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
#
# list3=[name +":" +ad[2:] for ad in list1 for name in list2 if ad[0]==name[0]]
#
# for i in list3:
#     print(i)

#格式化输出
#
# num=input('请输入一个整数（输入Q结束程序）：')
#
# while True:
#     if num=="Q":
#         print('程序结束')
#         break
#     else:
#         num=int(num)
#         print('十进制->十六进制：%d -> 0x%x'%(num,num))
#         print('十进制->八进制：%d -> 0o%o' % (num, num))
#         print('十进制->二进制：%d -> %s' % (num, bin(num)))
#         break

#max
# def max():
#     num=[1,2,3,4]
#     max=num[0]
#     for i in num:
#         if i>max:
#             max=i
#     return max
#
# print(max())
#
# def min():
#     num=[1,2,3,4]
#     least=num[0]
#     for i in num:
#         if i<least:
#             least=i
#     return least
#
# print(min())

#
# score=[['黑夜','89'],['小白','80'],['米兔','90']]
# target=input('请输入你要查找的名字：')
# isfind=False
# for i in score:
#     if target in i:
#         isfind=True
#         print('%s的成绩为：%s'%(target,i[1]))
# if isfind==False:
#     print('你所查找的成绩不存在！！')

# list1=[1,3,'abc','1.2',1.5]
# def sum_plus(num):
#     sum=0
#     for i in list1:
#         if type(i)==int or type(i)==float:
#             sum+=i
#         else:
#             continue
#     return sum
#
# print(sum_plus(list1))

#求次方的函数
# def power(x,y):
#     result2=1
#
#     for i in range(y):
#         result2*=x
#
#     return result2
#
# print(power(2,0))

#几欧里得求最大公约数
#
# def gcd_a(x,y):
#     while y:
#         t=x%y
#         x=y
#         y=t
#     return x
#
# print(gcd_a(1997,615))

#十进制转换二进制
# def bin_test(x):
#     tmp=[]
#     result2=''
#     while x:
#         t=x//2
#         target=x%2
#         x=t
#         tmp.append(target)
#
#
#
#     for i in tmp:
#         result2+=str(i)
#
#     return result2
#
# print(bin_test(108))


#
# def Dec2Bin(dec):
#     temp = []
#     result2 = ''
#
#     while dec:
#         quo = dec % 2
#         dec = dec // 2
#         temp.append(quo)
#
#     while temp:
#         result2 += str(temp.pop())
#
#     return result2
#
# print(Dec2Bin(64))


# def sum_canshu(*tests):
#     test=[]
#     length=len(tests)
#     sum=0
#     for i in tests:
#         test.append(i)
#
#     if test[length-1]==5:
#         for i in test:
#             if i%2!=0:
#                 sum+=i
#         sum*=5
#     else:
#         for i in test:
#             try:
#                 sum+=i
#             except TypeError:
#                 print('无视字符串妨碍！！')
#
#         sum*=3
#     return sum
#
# print(sum_canshu(1,2,3,'a'))


#100到999水仙花数的求法，写成函数

# def shuixianhua():
#     print('100到999的水仙花有：',end='')
#     for i in range(100,1000):
#         bai=i//100
#         shi=i%100//10
#         ge=i%100%10
#
#         if bai**3+shi**3+ge**3==i:
#             print(i,end=' ')
#
# shuixianhua()

# '''
# 1.需要传入两个参数，一个是要查找的字符，一个是被查找的内容
# 2.要统计字符串的出现次数
# 3.打印一句话说明一共多少次
# '''
# def isfind(target,content):
#     times=content.count(target)
#
#     print('目标字符【%s】一共在内容【%s】中出现了%d次'%(target,content,times))
#
# target='improver'
# content='You cannot improve your past,but you can improve your future.' \
#         '\tOnce time is wasted,life is wasted.'
# isfind(target,content)


# 5的阶乘
# def jiecheng(n):
#     result2 = 1
#     for i in range(1, n + 1):
#         result2 *= i
#
#     return result2
#
#
# print(jiecheng(5))

#用递归写一个x的y次幂的计算函数
# def power(x,y):
#     result2=0
#     if y==0:
#         x=1
#         return x
#     else:
#         if y>1:
#             return power()

# #求x的y次幂
# def power(x, y):
#     if y==0:
#         return 1
#     else:
#         return x*power(x,y-1)
#
#
# print(power(2, 2))

#递归版求最大公约数
# def gcd(x, y):
#     if y:
#         return gcd(y, x % y)
#     else:
#         return x
#
# print(gcd(4, 6))

#递归版斐波那契数列
# def fab(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
#
# print(fab(5))

#迭代版斐波那契数列
# def fab(n):
#     n1=1
#     n2=1
#     n3=2
#     if n==1 or n==2:
#         return 1
#     while n>2:
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         n-=1
#     return n3
#
# print(fab(10))

#递归求解汉诺塔游戏解法
# def han(n,x,y,z):
#     if n==1:
#         print(x,'-->',z)
#     else:
#         han(n-1,x,z,y)
#         print(x,"-->",z)
#         han(n-1,y,x,z)
#
# han(3,'x','y','z')

#递归求解二进制bin的实现
# def Dec2Bin(dec):
#     result2 = ""
#
#     if dec:
#         result2 = Dec2Bin(dec // 2)
#         return result2 + str(dec % 2)
#     else:
#         return result2
#
#
# print(Dec2Bin(128))


#获取变量的每个位数的数字存放到列表
# result2 = []
# def get_digit(n):
#     if n>0:
#         get_digit(n // 10)
#         result2.append(n % 10)
#
#
#
# get_digit(12345)
#
# print(result2)

#年龄倒推：
# def age(n):
#     if n!=1:
#         return age(n-1)+2
#     else:
#         return 10
#
# print(age(5))
#
#
# psw=input('请输入需要检查的密码组合：')
# zimu=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C'
#       , 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
# shuzi='1234567890'
# fuhao='`~!@#$%^&*()-_+={}[]|\'\;:<>,./?"'
# length=len(psw)
# while psw.isspace()or length==0:
#     print('你输入的密码为空（只包含空格），请重新输入：',end='')
#     psw=input()
#     length=len(psw)
#
# if length<=8:
#     num_level=1
#
# elif 8<length<16:
#     num_level=2
# else:
#     num_level=3
#
# str_level=0
# for i in psw:
#     if i in zimu:
#         str_level+=1
#         break
#
# for i in psw:
#     if i in fuhao:
#         str_level += 1
#         break
#
# for i in psw:
#     if i in shuzi:
#         str_level += 1
#         break
#
# while 1:
#     if num_level==1 or str_level==1:
#         print('安全等级为：低')
#     elif num_level==2 or str_level==2 :
#         print('安全等级为：中')
#     elif (num_level==3 or str_level==3)and not psw.startswith(zimu):
#         print('安全等级为：较高')
#     else:
#         print('安全等级为：高\n请继续保持')
#         break
#     print('1.密码必须由数字、字母、特殊字符三种组合\n2.密码长度不能低与16位\n3.请以字母开头')
#     breakpsw=input('请输入需要检查的密码组合：')
# zimu=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','A','B','C'
#       , 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
# shuzi='1234567890'
# fuhao='`~!@#$%^&*()-_+={}[]|\'\;:<>,./?"'
# length=len(psw)
# while psw.isspace()or length==0:
#     print('你输入的密码为空（只包含空格），请重新输入：',end='')
#     psw=input()
#     length=len(psw)
#
# if length<=8:
#     num_level=1
#
# elif 8<length<16:
#     num_level=2
# else:
#     num_level=3
#
# str_level=0
# for i in psw:
#     if i in zimu:
#         str_level+=1
#         break
#
# for i in psw:
#     if i in fuhao:
#         str_level += 1
#         break
#
# for i in psw:
#     if i in shuzi:
#         str_level += 1
#         break
#
# while 1:
#     if num_level==1 or str_level==1:
#         print('安全等级为：低')
#     elif num_level==2 or str_level==2 :
#         print('安全等级为：中')
#     elif (num_level==3 or str_level==3)and not psw.startswith(zimu):
#         print('安全等级为：较高')
#     else:
#         print('安全等级为：高\n请继续保持')
#         break
#     print('1.密码必须由数字、字母、特殊字符三种组合\n2.密码长度不能低与16位\n3.请以字母开头')
#     break

# a=0
# while a<10:
#     if a%2!=0:
#         print(a)
#         continue
#     a+=2
#     print(a)

# for i in range(10):
#     if i%2 !=0:
#         print(i)
#         continue
#     i+=2
#     print(i)

#复盘暗语1
# def findStr():
#     file1=open('Ar_Script/resources/string1.txt')
#     str1=''
#     tmp=[]
#     for i in file1:
#         str1+=i
#
#     for i in str1:
#         # if i not in tmp:
#         #     if i=='\n':
#         #         print('\\n:',str1.count(i))
#         #     else:
#         #         print(i+':',str1.count(i))
#         #     tmp.append(i)
#         print(i,end='')
#     file1.close()
#
# findStr()


# 复盘暗语2
# def findStr():
#     file1 = open('Ar_Script/resources/string2.txt')
#     str1 = ''
#     # str1='ABCaAVSaAVX'
#     countA=0
#     countB=0
#     countC=0
#
#     for i in file1:
#         str1+=i
#
#     for i in str1:
#         print(i)
#
#     length = len(str1)
#
#     for i in range(length):
#         if str1[i]=='\n':
#             continue
#
#         if str1[i].isupper():
#             if countB:
#                 countC+=1
#             else:
#                 countC=0
#                 countA+=1
#
#         if str1[i].islower():
#             if countA!=3:
#                 countA = 0
#                 countB = 0
#                 countC = 0
#             else:
#                 if countB:
#                     countA = 0
#                     countB = 0
#                     countC = 0
#                 else:
#                     countB=1
#                     countC=0
#                     target=i
#
#         if countA==3 and countC==3:
#             if i+1!=length and str1[i+1].isupper():
#                 countB=0
#                 countC=0
#             else:
#                 print(str1[target],end='')
#                 countA=3
#                 countB=0
#                 countC=0
#     file1.close()
#
# findStr()

import random as r
#
# legal_x = [0, 10]
# legal_y = [0, 10]
#
#
# class Turtle:
#     def __init__(self):
#         # 初始体力
#         self.power = 100
#         # 初始位置随机
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, 2, -1, -2])
#         new_y = self.y + r.choice([1, 2, -1, -2])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#             # 体力消耗
#         self.power -= 1
#         # 返回移动后的新位置
#         return (self.x, self.y)
#
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
#
#
# class Fish:
#     def __init__(self):
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置（x, y）
#         new_x = self.x + r.choice([1, -1])
#         new_y = self.y + r.choice([1, -1])
#         # 检查移动后是否超出场景x轴边界
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         # 检查移动后是否超出场景y轴边界
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#         # 返回移动后的新位置
#         return (self.x, self.y)
#
#
# turtle = Turtle()
# fish = []
# for i in range(10):
#     new_fish = Fish()
#     fish.append(new_fish)
#
# while True:
#     if not len(fish):
#         print("鱼儿都吃完了，游戏结束！")
#         break
#     if not turtle.power:
#         print("乌龟体力耗尽，挂掉了！")
#         break
#
#     pos = turtle.move()
#     print('\n乌龟现在的所在位置为：',turtle.x,turtle.y)
#     # print(new_fish.x,new_fish.y)
#     # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
#     # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
#     for each_fish in fish[:]:
#         if each_fish.move() == pos:
#             # 鱼儿被吃掉了
#             turtle.eat()
#             fish.remove(each_fish)
#             # print('所剩下的鱼儿数量：%d'%(len(fish)))
#             # print('乌龟坐在位置：',turtle.x, turtle.y)
#             print('被吃鱼儿所在位置：',each_fish.x,each_fish.y)
#             print("有一条鱼儿被吃掉了...")
#             # print('所剩下的鱼儿数量：%d' % (len(fish)))
#         else:
#             print('其他鱼儿的位置：',each_fish.x,each_fish.y)

