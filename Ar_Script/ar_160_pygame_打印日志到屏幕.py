import pygame
import sys

pygame.init()

size=width,height=600,400

bg=(0,0,0)

screen=pygame.display.set_mode(size)

pygame.display.set_caption('打印日志到屏幕')

'创建一个文字的surface对象'
font=pygame.font.Font(None,20)

line_height=font.get_linesize()
position=0



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
        position+=line_height

        if position>height:
            screen.fill(bg)
            position=0

        pygame.display.flip()