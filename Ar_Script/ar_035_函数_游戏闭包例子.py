#这是一个游戏闭包的例子

origin=(0,0)
legal_x=[-100,100]
legal_y=[-100,100]
#这个写成了[100,100]，哎哟我去，还好debug跑出来了
#我是觉得没有必要急着对答案吧，先debug没准还是能发现公式的错误的
#自己对于自己还是太没有自信，一看到不认识的就慌

def position(pos_x=0,pos_y=0):

    def moving(direction,step):
        nonlocal pos_x,pos_y

        new_x=pos_x+direction[0]*step
        new_y=pos_y+direction[1]*step
        '''这竟然计算公式写错了一次'''

        if new_x<legal_x[0]:
            pos_x=legal_x[0]-(new_x-legal_x[0])
        elif new_x>legal_x[1]:
            pos_x=legal_x[1]-(new_x-legal_x[1])
        else:
            pos_x=new_x

        '''又一次没有将角标带上，对于列表参数自己的警惕性不够'''
        if new_y<legal_y[0]:
            pos_y=legal_y[0]-(new_y-legal_y[0])
        elif new_y>legal_y[1]:
            pos_y=legal_y[1]-(new_y-legal_y[1])
        else:
            pos_y=new_y

        return pos_x,pos_y
    return moving

move=position()
# 避免写成position()([1,0],90))这样比较麻烦，也会让人知道这是闭包实现
print('向右移动90的坐标为：',move([1,0],90))
print('向左移动40的坐标为：',move([-1,0],40))
print('向上移动30的坐标为：',move([0,1],30))