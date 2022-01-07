import pygame
import sys


tiles = 11
tile_size = 64

screen_height = tiles * tile_size
screen_width = 1200

screen = pygame.display.set_mode((screen_width,screen_height))

running = True

idle_char = pygame.image.load('/Users/greninja028/Desktop/Coding/contra/BillRizerRuns.png').convert_alpha()
# idle_char = pygame.transform.scale(screen, (1,1))
idle_char_pos_x, idle_char_pos_y = screen_width//2, 0

GRAVITY = 1

clock = pygame.time.Clock()
rect_platform = pygame.Rect(0, 234, 1200, 25)

def load_images():
    global idle_char
    screen.blit(idle_char, (idle_char_pos_x, idle_char_pos_y))

# def test():

def check_collision():
    global rect_platform
    pygame.draw.rect(screen, (255, 255, 255), rect_platform)
    rect = idle_char.get_rect()
    player_collided = pygame.Rect.colliderect(rect, rect_platform)
    if player_collided:
        rect.bottom = rect_platform.top

def main():

    FPS = 60

    global running, idle_char, idle_char_pos_x, idle_char_pos_y, rect_platform
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            screen.fill('black')
            load_images()
        check_collision()

        idle_char_pos_y += GRAVITY

        keys = pygame.key.get_pressed()


        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            idle_char_pos_x += 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            idle_char_pos_x -= 5
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            idle_char_pos_y -= 5

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()