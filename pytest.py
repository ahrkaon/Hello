import pygame
from random import *
import sys

pygame.init()

swidth = 480
sheight = 640
screen = pygame.display.set_mode((swidth,sheight))

pygame.display.set_caption("game")

#배경 이미지
background = pygame.image.load("D:\\Python_Workspace\\py_workspace\\background.png")
#몬스터


#캐릭터 불러오기
character = pygame.image.load("D:\\Python_Workspace\\py_workspace\\character.png")
character_size = character.get_rect().size
cwidth = character_size[0]
cheight = character_size[1]
c_x_pos = (swidth / 2) - (cwidth / 2)
c_y_pos = sheight - cheight

to_x = 0
to_y = 0

running = True
while running:
    (pygame.time.Clock().tick(50))
#캐릭터이동
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT : 
                to_x -= 2
            elif event.key == pygame.K_RIGHT : 
                to_x += 2
            elif event.key == pygame.K_UP : 
                to_y -= 2
            elif event.key == pygame.K_DOWN : 
                to_y += 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0
        
    #screen.fill((0,0,255))
    screen.blit(background, (0,0))
    screen.blit(character, (c_x_pos,c_y_pos))

    c_x_pos += to_x
    c_y_pos += to_y

    if c_x_pos < 0:
        c_x_pos = 0
    elif c_x_pos > swidth - cwidth:
        c_x_pos = swidth - cwidth
    
    if c_y_pos < 0:
        c_y_pos = 0
    elif c_y_pos > sheight - cheight:
        c_y_pos = sheight - cheight
    
    
    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()