print()
'尝试将文件(openme.mp3)打印到屏幕上'
f1=open('resources/OpenMe.mp3')
f2=open('result/OpenMe.txt','w',encoding='utf-8')


for i in f1:
    print(i)

# print(f1.read())

# f.close()
'要将f1的文本位置重置到第一个字符，不然刷了一遍之后就没有东西写进去了'
f1.seek(0)

'编写代码，将上一题中的文件保存为新的txt文件'
f2.write(f1.read())

f2.close()
f1.close()