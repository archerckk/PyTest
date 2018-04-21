import easygui as g
import sys

result=g.boolbox(msg='请问要继续嘛？',choices=['是','否'],title='是否继续')

print(result)