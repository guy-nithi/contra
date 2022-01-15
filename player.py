from xml.dom.minidom import CharacterData
import pygame

class Player:
    def __init__(self, position, surface):
        super().__init__()
        self.char_assets()
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def char_assets(self):
        character_path = './assets/'
        self.animations = {'idle':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            # self.animations[animation] = import_folder(fulll_path)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y