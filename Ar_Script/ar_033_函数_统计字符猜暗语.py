import os

# 统计下边这个长字符串中出现的次数并找出隐藏在里面的一句话

def findStr():
    target = open('resources/string1.txt')
    str1 = ""
    list1 = []
    for i in target:  # 之前直接用str（）工厂函数生成，整个文件内容就不对了，还是遍历再添加会好一些
        str1 += i

    for i in str1:
        if i not in list1:  # 检查是否已经统计过次数
            if i == '\n':  # 针对换行符的统计
                print('\\n:', str1.count(i))#打印\n需要转义，对应的统计次数
            else:
                print(i + ':', str1.count(i))
            list1.append(i)  # 避免不会统计到重复的内容，每一个字符只有一次统计


findStr()
