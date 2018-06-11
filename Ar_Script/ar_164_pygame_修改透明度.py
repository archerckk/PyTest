import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 600, 400
bg = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('裁剪demo')

background = pygame.image.load('resources/background.jpg').convert()
turtle = pygame.image.load('resources/turtle.png').convert_alpha()

position = turtle.get_rect()
'???'
position.center = width // 2, height // 2


def blit_alpha(bg, target, location, ratio):
    x = location[0]
    y = location[1]
    # '先画一个空的对象surface对象'
    temp = pygame.Surface((target.get_width(), target.get_height())).convert()

    temp.blit(bg, (-x, -y))
    temp.blit(target, (0, 0))
    temp.set_alpha(ratio)
    bg.blit(temp, location)


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.blit(background, (0, 0))

    blit_alpha(screen, turtle, position, 200)

    pygame.display.flip()
