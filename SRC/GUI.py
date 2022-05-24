import pygame
from entity import *

class GUI:

    def __init__(self):
        self.box = pygame.image.load('GUI/gui.png')

    def render(self, screen):
        screen.blit(self.box, (30, 100))


class GUI_sword:

    def __init__(self):
        self.box = pygame.image.load('GUI/gui_sword.png')

    def render(self, screen):
        screen.blit(self.box, (30, 100))


class GUI_flute:

    def __init__(self):
        self.box = pygame.image.load('GUI/gui_flute.png')

    def render(self, screen):
        screen.blit(self.box, (30, 100))


class GUI_both:

    def __init__(self):
        self.box = pygame.image.load('GUI/gui_both.png')

    def render(self, screen):
        screen.blit(self.box, (30, 100))


class full_health:

    def __init__(self):
        self.box = pygame.image.load('GUI/full_health.png')

    def render(self, screen):
        screen.blit(self.box, (30, 30))


class low_health:

    def __init__(self):
        self.box = pygame.image.load('GUI/low_health.png')

    def render(self, screen):
        screen.blit(self.box, (30, 30))


class full_shield_health:

    def __init__(self):
        self.box = pygame.image.load('GUI/full_shield_health.png')

    def render(self, screen):
        screen.blit(self.box, (30, 30))
