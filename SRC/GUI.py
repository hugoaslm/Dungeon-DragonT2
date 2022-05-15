import pygame
from entity import *


class GUI_health:

    def __init__(self):
        self.gui = pygame.display.set_mode((1280, 720))
        self.skeleton1 = Skeleton1()

    def render(self, screen):
        gui_color = (111, 210, 66)
        gui_color_bg = (70, 20, 72)
        gui_position = [self.skeleton1.position[0] + 10, self.skeleton1.position[1] - 20, self.skeleton1.health, 5]
        gui_bg_position = [self.skeleton1.position[0] + 10, self.skeleton1.position[1] - 20, self.skeleton1.max_health,
                           5]
        pygame.draw.rect(screen, gui_color_bg, gui_bg_position)
        pygame.draw.rect(screen, gui_color, gui_position)


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
