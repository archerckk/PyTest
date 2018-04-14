#一次打印列表当中的两个内容
test=['test1',1,'test2',2,'test3',3]
length=len(test)
for i in range(0,length,2):
    print(test[i],test[i+1])

#TypeError: range() does not take keyword arguments
#range不能带关键字参数
a=0
while 1:
   if a<length:
        print(test[a],test[a+1])
        a += 2
   else:
       break
#参考答案的写法其实就是比我写的精简一些吧，说明自己理解还是不太够啊
#参考答案：
while a<length:
    print(test[a],test[a+1])
    a+=2
