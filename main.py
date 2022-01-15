import pygame
import sys
from random import *
from settings import *
from level import Level

# Pygame stuff
screen = pygame.display.set_mode((screen_width,screen_height))
running = True
idle_char = pygame.image.load('/Users/greninja028/Desktop/Coding/contra/assets/BillRizerRuns.png').convert_alpha()
idle_char_pos_x, idle_char_pos_y = 0, screen_height//2
level = Level(map,screen)

clock = pygame.time.Clock()
rect_platform = pygame.Rect(0, 234, 1200, 25)

screen.blit(idle_char, (idle_char_pos_x, idle_char_pos_y))

FPS = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
        screen.fill('black')

    pygame.display.update()
    clock.tick(FPS)