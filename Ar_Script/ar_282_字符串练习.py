import string
import sys

# with open('testStr.txt','w')as f:
#     '测试代码'
#     # content=str(help(string))
#     # f.write(content)


f=open('testStr.txt','w')
sys.stdout=f
help(string)
f.close()
f=open('testStr.txt','r')
sys.stdout.write(f.read())
# print()


