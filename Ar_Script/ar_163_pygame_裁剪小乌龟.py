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
position.center=width//2,height//2

while 1:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()



    screen.fill(bg)

    screen.blit(turtle,position)

    pygame.display.flip()
