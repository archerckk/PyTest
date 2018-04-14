'这是一个格式化文字的游戏'

girl_list=['小皮球','小皮蛋','小学森','吕梅清','小宝宝','大懒猪','懒训猪','梅清','笨猪','大笨猪','皮蛋','皮球']
boy_list=['外星人','臭臭','陈智斌','臭猪','智斌','斌斌','斌']


girl=input('请输入你的名字：')
while girl not in girl_list:
    print('你输入你的名字有误，请重新输入：',end='')
    girl=input()

boy=input('请输入你爱的人的名字：')
while boy not in boy_list:
    print('你输入的爱人名字有误，请重新输入：',end='')
    boy=input()

print('%s爱%s一生一世'%(girl,boy))
input()