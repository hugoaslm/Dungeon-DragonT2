import pygame
import os


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'sprites/{name}.png')
        self.animation_index = 0
        self.clock = 0
        self.images = {
            "up": self.get_images(97),
            "down": self.get_images(0),
            "right": self.get_images(65),
            "left": self.get_images(33),
            "attack_down": self.get_images60(145),
            "attack_left": self.get_images60(210),
            "attack_right": self.get_images60(276),
            "attack_up": self.get_images60(342)
        }
        self.speed = 3

    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey(0, 0)
        self.clock += self.speed * 8

        if self.clock >= 100:

            self.animation_index += 1  # passer à l'image suivante

            if self.animation_index >= 6:
                self.animation_index = 0

            self.clock = 0

    def get_images(self, y):
        images = []

        for i in range(0, 8):
            x = i * 48
            image = self.get_image(x, y)
            images.append(image)

        return images

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def get_images60(self, y):
        images60 = []

        for i in range(0, 6):
            x = i * 61
            image = self.get_image60(x, y)
            images60.append(image)

        return images60

    def get_image60(self, x, y):
        image = pygame.Surface([60, 60])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 60, 60))
        return image

    def change_animation60(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey(0, 0)
        self.clock += self.speed * 8

        if self.clock >= 100:

            self.animation_index += 1  # passer à l'image suivante

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0
