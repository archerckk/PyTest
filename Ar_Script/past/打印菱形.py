tmp=int(input('请输入你要输入最多一行的星星数：'))
s = '*'
for i in range(1,tmp+1,2):
    t = (tmp-i)//2
    print(' '*t + s*i + ' '*t)
for i in reversed(range(1,tmp-1,2)):
    t = (tmp-i)//2
    print(' '*t + s*i + ' '*t)


# num=int(input('请你输入一个数字：'))
# image='*'
# for i in range(1,num+1,2):
#     t=(num-i)//2
#     print(' '*t+image*i)
# for i in reversed(range(1,num-1,2)):
#     t = (num - i) // 2
#     print(' '*t+image*i)


# print()
# while num:
#     print(' '*num+image*num)
#     num-=1

# for i in reversed(range(0,num,1)):
#     print(' '*i + image*i )