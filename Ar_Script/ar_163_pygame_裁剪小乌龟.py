import pygame
import sys
from pygame.locals import *


pygame.init()

size=width,height=600,400
bg=(255,255,255)

screen=pygame.display.set_mode(size)
pygame.display.set_caption('裁剪demo')

turtle=pygame.image.load('resources/turtle.png')

position=turtle.get_rect()
'???'
position.center=width//2,height//2

'0:未选中，1：选择中，2：选择完毕'
select=0
select_rect=pygame.Rect(0,0,0,0)
'0:未拖拽，1：拖拽中，2：拖拽完毕'
drag=0


while 1:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()

        '响应鼠标左键点击'
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                '记录下第一下单击鼠标时的位置'
                if select==0 and drag==0:
                    pos_start=event.pos
                    select=1


        elif event.type==MOUSEBUTTONUP:
            if select==1 and drag==0:
                pos_stop=event.pos
                select=2


    screen.fill(bg)

    screen.blit(turtle,position)

    if select:
        mouse_pos=pygame.mouse.get_pos()
        if select==1:
            pos_stop=mouse_pos
        select_rect.left,select_rect.top=pos_start
        select_rect.width,select_rect.height=pos_stop[0]-pos_start[0],pos_stop[1]-pos_start[1]
        pygame.draw.rect(screen,(0,0,0),select_rect,1)





    pygame.display.flip()
