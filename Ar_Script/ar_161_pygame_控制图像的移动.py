import pygame
from pygame.locals import *
import sys

pygame.init()

size=width,height=600,400
bg=(255,255,255)
speed=[-2,1]

'新建一个显示窗口'
screen=pygame.display.set_mode(size,RESIZABLE)
pygame.display.set_caption('移动的小乌龟')

'原始图片备份，加载图片，获取图片的位置'
ratio=1
oturtle=pygame.image.load('resources/turtle.png')
turtle=oturtle
oturtle_rect=oturtle.get_rect()
position=turtle_rect=oturtle_rect

'设置图片的两个方向'
left_head=turtle
right_head=pygame.transform.flip(turtle,True,False)

'设置全屏开关'
fullscreen=False





while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()

        '响应键盘的上下左右键'
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                turtle=left_head
                speed=[-1,0]
            if event.key==K_RIGHT:
                turtle=right_head
                speed=[1,0]
            if event.key==K_UP:
                speed=[0,-1]
            if event.key==K_DOWN:
                speed=[0,1]

            '增加全屏切换功能'
            if event.key==K_F11:
                fullscreen=not fullscreen
                if fullscreen:
                    screen=pygame.display.set_mode(pygame.display.list_modes()[0],FULLSCREEN|HWSURFACE)
                    width,height=pygame.display.list_modes()[0]
                else:
                    screen = pygame.display.set_mode(size)
                    width,height=size
                    position = turtle.get_rect()

            if event.key==K_MINUS or event.key==K_EQUALS or event.key==K_SPACE:
                if event.key==K_EQUALS and ratio<2:
                    ratio+=0.1
                elif event.key==K_MINUS and ratio>0.5:
                    ratio-=0.1
                else:
                    ratio=1

                turtle=pygame.transform.smoothscale(oturtle,
                                                    (int(oturtle_rect.width*ratio),
                                                     (int(oturtle_rect.height*ratio)))
                                                    )
                left_head=turtle
                right_head=pygame.transform.flip(turtle,True,False)

        '增加改变窗口大小功能'
        if event.type==VIDEORESIZE:
            size=event.size
            width,height=size
            print(size)
            screen = pygame.display.set_mode(size,RESIZABLE)



    position=position.move(speed)

    '判断乌龟移动的边界'
    if position.left<0 or position.right>width:
        '假如这里换成right_head的话是不能实现图像的翻转的'
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0]=-speed[0]
    if position.top<0 or position.bottom>height:
        speed[1]=-speed[1]

    '填充背景颜色'
    screen.fill(bg)
    '更新图像和位置'
    screen.blit(turtle,position)
    '更新整个界面'
    pygame.display.flip()
    '设置延迟'
    pygame.time.delay(10)


