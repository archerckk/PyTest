import time as t

class Mytimer:

    def __str__(self):
        return self.toast

    def __add__(self, other):
        toast = '总共运行了'
        result=[]
        for i in range(6):
            result.append(self.result[i] + other.result[i])
            if result[i]:
                toast += str(result[i]) + self.unit[i]
        print(toast)

    __repr__=__str__

    def __init__(self):
        self.begin=0
        self.end=0
        self.toast='未开始计时器'
        self.unit=['年','月','日','时','分','秒']
        self.result=[]

    def start(self):
        self.toast='请先停止计时器'
        self.begin=t.localtime()
        print('开始计时')

    def stop(self):
        if not self.begin:
            self.toast='请先开始计时！'
        else:
            self.end=t.localtime()
            self._calresult()
            print('结束计时')

    def _calresult(self):
        self.toast='总共运行了'
        for i in range(6):
            self.result.append(self.end[i]-self.begin[i])
            if self.result[i]:
                self.toast+=str(self.result[i])+self.unit[i]
        print(self.toast)

        #重新初始化数据
        self.begin=0
        self.end=0