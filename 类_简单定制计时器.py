import time

class My_timer:

    def __init__(self):
        self.begin=0
        self.end=0
        self.lasted=[]
        self.prompt='未开始计时！'
        self.unit=['年','月','天','时','分','秒']

    def __str__(self):
        return self.prompt

    def __add__(self, other):
        prompt='总共运行了'
        result=[]
        for i in range(6):
            result.append(self.lasted[i]+other.lasted[i])
            if result[i]:
                prompt+=str(result[i])+self.unit[i]
        return prompt

    __repr__=__str__

    def start(self):
        self.begin=time.localtime()
        self.prompt='请先停止计时'
        print('计时开始……')

    def stop(self):
        if not self.begin:
            print('请先运行start()')
        else:
            self.end=time.localtime()
            self.caltime()
            print('计时结束!!')

    def caltime(self):
        self.prompt='总共运行了'
        for i in range(6):
            self.lasted.append(self.end[i]-self.begin[i])
            if self.lasted[i]:
                self.prompt+=str(self.lasted[i])+self.unit[i]
        return self.prompt




