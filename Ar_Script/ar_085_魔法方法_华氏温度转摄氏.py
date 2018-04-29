'''
1 按照以下要求，定义一个类实现摄氏到华氏度的转换（转换公式=摄氏度*18+32）
'''

#方向就不对……
class Cf:

    def __init__(self,tmp):
        self.tmp=self.getTep(tmp)


    def getTep(self,a):
        self.tmp=a*1.8+32

cf=Cf(32)
print(cf.tmp)

'在实例化之后，再计算的话，就显示不出来结果的了，显示出来的是一个生成器'

#参考答案：
class C2F(float):
    "摄氏度转换为华氏度"

    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg * 1.8 + 32)

print(C2F(32))
