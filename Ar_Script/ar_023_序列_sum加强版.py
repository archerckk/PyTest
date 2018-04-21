test=[1,222,'sss','aaaa',10]
sum=0
for i in test:
    if isinstance(i,int) or isinstance(i,float):
        sum+=i
    else:
        continue
print(sum)

#参考答案
# def sum(x):
#     result2 = 0
#
#     for each in x:
#         if (type(each) == int) or (type(each) == float):
#             result2 += each
#         else:
#             continue
#
#     return result2
#
#
# print(sum([1, 2.1, 2.3, 'a', '1', True]))