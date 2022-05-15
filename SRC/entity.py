import pygame
from Animation import *
import Game_2


class Entity(AnimatedSprite):

    def __init__(self, name, x, y):
        super().__init__(name)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def save_location(self):
        self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def move_up(self):
        self.position[1] -= self.speed


class Player(Entity):

    def __init__(self):
        super().__init__("KnightWW", 3010.32, 1431.93)
        self.rect = self.image.get_rect()


class Skeleton1(Entity):

    def __init__(self):
        super().__init__("Skeleton", 1952, 1120)
        self.rect = self.image.get_rect()
        self.health = 10
        self.max_health = 10
        self.attack = 5

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 2000


class Skeleton2(Entity):

    def __init__(self):
        super().__init__("Skeleton", 2272.00, 1248.00)
        self.rect = self.image.get_rect()
        self.health = 100
        self.max_health = 100
        self.attack = 5


class Skeleton3(Entity):

    def __init__(self):
        super().__init__("Skeleton", 1920, 1376)
        self.health = 100
        self.max_health = 100
        self.attack = 5


class DragonPixel(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('sprites/dragon_jaune128.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([128, 192])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 128, 192))
        return image


class Minotaur(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('sprites/Minotaur.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([128, 100])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 128, 100))
        return image
