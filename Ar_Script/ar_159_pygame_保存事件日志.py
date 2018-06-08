import pygame
import sys

pygame.init()

size=width,height=600,400

pygame.display.set_mode(size)
f=open('result/game_record.txt','w')

while True:
    for event in pygame.event.get():
        f.write(str(event)+'\n')
        if event.type==pygame.QUIT:
            f.close()
            sys.exit()