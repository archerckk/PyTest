a='abcd'
b=[1,2,3,4]
'可变的数据类型'
c=('a','b','c')
d={'key':'value','key2':'value2'}

"""
sorted方法key用法
1.用string.upper这个方法，去执行列表里的每一个数据，也就是说，
"""


#
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}

"""
2.1 迭代字典，输出结果：
('a', 'haha')
('c', 'hehe')
('b', 'python')
('f', 'xiaoming')
"""
listTemp=list(ainfo.keys())
listTemp.sort()
listTemp.insert(0,'b')

for key,value in ainfo.items():
    print((key,value))