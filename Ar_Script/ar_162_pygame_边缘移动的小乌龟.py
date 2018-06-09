import pygame
import sys
from pygame.locals import *

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
pygame.display.set_caption('边缘移动的小乌龟')

'加载图片'
turtle = pygame.image.load("resources/turtle.png")
position=turtle.get_rect()

'设置全屏开关为关'
fullscreen=False


'获取图片方向'
turtle_right=pygame.transform.rotate(turtle,90)
turtle_top=pygame.transform.rotate(turtle,180)
turtle_left=pygame.transform.rotate(turtle,270)
turtle_buttom=turtle
turtle=turtle_top

'图片的循环移动'
while True:
    '假如事件类型为退出，则退出游戏'
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        '增加全屏切换功能'
        if event.type==KEYDOWN:
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(pygame.display.list_modes()[0], FULLSCREEN | HWSURFACE)
                    width, height = pygame.display.list_modes()[0]
                else:
                    screen = pygame.display.set_mode(size)
                    width, height = size
                    position = turtle.get_rect()

    '移动图像'
    position = position.move(speed)

    '移动的边界检测，假如到达边界则反向移动'
    if position.right>width:
        turtle=turtle_right
        position=turtle_rect=turtle.get_rect()
        position.left=width-turtle_rect.width
        speed=[0,5]

    if position.bottom>height:
        turtle=turtle_buttom
        position=turtle_rect=turtle.get_rect()
        position.left=width-turtle_rect.width
        position.top=height-turtle_rect.height
        speed=[-5,0]

    if position.left<0:
        turtle=turtle_left
        position=turtle_rect=turtle.get_rect()
        position.top=height-turtle_rect.height
        speed=[0,-5]

    if position.top<0:
        turtle=turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5, 0]

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

