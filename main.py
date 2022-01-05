import pygame
import sys
import time

tiles = 11
tile_size = 64

screen_height = tiles * tile_size
screen_width = 1200

screen = pygame.display.set_mode((screen_width,screen_height))

running = True

idle_char = pygame.image.load('/Users/greninja028/Desktop/Coding/contra/1.png').convert_alpha()
idle_char_pos_x, idle_char_pos_y = screen_width//2, screen_height//2

gravity = 1

def load_images():
    global idle_char
    screen.blit(idle_char, (idle_char_pos_x, idle_char_pos_y))

def main():
    global running, idle_char, idle_char_pos_x, idle_char_pos_y
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            screen.fill('black')
            idle_char_pos_y += gravity
            load_images()

            # pygame.display.update()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            idle_char_pos_x += 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            idle_char_pos_x -= 5
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            idle_char_pos_y -= 5

        pygame.display.update()

if __name__ == '__main__':
    main()