import pygame
import sys

#
'初始化pytgame模块'
pygame.init()

'定义边界，移动方向幅度，背景颜色'
size=width,height=600,400
speed=[-2,1]
background=(255,255,255)#RGB

'设置背景大小'
screen=pygame.display.set_mode(size)

'设置标题'
pygame.display.set_caption('初次见面，请多多指教')

'加载图片'
turtle = pygame.image.load("resources/turtle.png")

'获取图片位置'
position=turtle.get_rect()

'图片的循环移动'
while True:
    '假如事件类型为退出，则退出游戏'
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    '移动图像'
    position = position.move(speed)

    '移动的边界检测，假如到达边界则反向移动'
    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(background)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10)

