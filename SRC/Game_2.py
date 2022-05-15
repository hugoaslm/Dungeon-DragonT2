import pygame
import pytmx
import pyscroll
from GUI import *
from entity import *


class Game:

    def __init__(self):

        # Démarrage
        self.running = True
        self.status = 0

        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Dungeon&Dragon")

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("Finalee.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Générer le joueur
        # player_position = tmx_data.get_object_by_name("Player")
        self.player = Player()
        self.gui_health = GUI_health()
        self.gui = GUI()
        self.gui_sword = GUI_sword()
        self.gui_flute = GUI_flute()
        self.gui_both = GUI_both()
        self.full_health = full_health()
        self.low_health = low_health()
        self.full_shield_health = full_shield_health()
        self.dragon_pixel = DragonPixel(1895, 295)
        self.minotaur = Minotaur(640, 256)

        # Générer le monstre
        self.skeleton1 = Skeleton1()
        self.skeleton2 = Skeleton2()
        self.skeleton3 = Skeleton3()

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "bnd":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.isles = []

        for obj in tmx_data.objects:
            if obj.type == "ile":
                self.isles.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.sword = []

        for obj in tmx_data.objects:
            if obj.type == "sword":
                self.sword.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.flute = []

        for obj in tmx_data.objects:
            if obj.type == "flt":
                self.flute.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.shield = []

        for obj in tmx_data.objects:
            if obj.type == "shield":
                self.shield.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.healing = []

        for obj in tmx_data.objects:
            if obj.type == "healing":
                self.healing.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.dragon = []

        for obj in tmx_data.objects:
            if obj.type == "drg":
                self.dragon.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.minotaur_isle = []

        for obj in tmx_data.objects:
            if obj.type == "mtr":
                self.minotaur_isle.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # self.swordF = []

        # for obj in tmx_data.objects:
        # if obj.type == "swd":
        # self.swordF.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=21)
        self.group.add(self.player)
        self.group.add(self.skeleton1)
        self.group.add(self.skeleton2)
        self.group.add(self.skeleton3)
        self.group.add(self.dragon_pixel)
        self.group.add(self.minotaur)

        # Porte de la maison
        # enter_house = tmx_data.get_object_by_name("enter_house")
        # self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    # def check_collision(self, sprite, group):

    # return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
            if pressed[pygame.K_w]:
                self.player.change_animation('attack_up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
            if pressed[pygame.K_w]:
                self.player.change_animation('attack_down')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
            if pressed[pygame.K_w]:
                self.player.change_animation('attack_right')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
            if pressed[pygame.K_w]:
                self.player.change_animation('attack_left')

    def game_over(self):
        self.status = 2

    def update(self):

        self.group.update()

        # Vérification des collisions
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()

        # Ecran d'accueil
        home_screen = pygame.image.load("MENU/home_screen.png")
        play_button = pygame.image.load("MENU/play_button.png")
        play_button_rect = play_button.get_rect()
        game_over = pygame.image.load("MENU/game_over.png")
        victory = pygame.image.load("MENU/victory.png")

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        self.status = 1

            if self.status == 1:
                self.player.save_location()
                self.handle_input()
                self.update()
                self.group.center(self.player.rect.center)
                self.group.draw(self.screen)
                self.full_health.render(self.screen)
                self.gui.render(self.screen)

                self.swordF = []
                if self.player.feet.collidelist(self.sword) > -1:
                    self.swordF = self.sword
                self.swordF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.sword) > -1:
                    self.gui_sword.render(self.screen)
                    if self.player.feet.collidelist(self.flute) > -1:
                        self.gui_both.render(self.screen)

                self.fluteF = []
                if self.player.feet.collidelist(self.flute) > -1:
                    self.fluteF = self.flute
                self.fluteF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.flute) > -1:
                    self.gui_flute.render(self.screen)
                    if self.player.feet.collidelist(self.sword) > -1:
                        self.gui_both.render(self.screen)

                self.HF = []
                if self.player.feet.collidelist(self.isles) > -1:
                    self.HF = self.isles
                self.HF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.isles) > -1:
                    self.low_health.render(self.screen)
                    if self.player.feet.collidelist(self.minotaur_isle) > -1:
                        self.game_over()
                    if self.player.feet.collidelist(self.dragon) > -1:
                        self.game_over()

                if self.player.feet.collidelist(self.healing) > -1:
                    self.HF = self.healing
                self.HF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.healing) > -1:
                    self.full_health.render(self.screen)
                    if self.player.feet.collidelist(self.minotaur_isle) > -1:
                        if self.player.feet.collidelist(self.flute) > -1:
                            self.running = True
                        else:
                            self.game_over()
                    if self.player.feet.collidelist(self.dragon) > -1:
                        self.game_over()

                if self.player.feet.collidelist(self.shield) > -1:
                    self.HF = self.shield
                self.HF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.shield) > -1:
                    self.full_shield_health.render(self.screen)
                    if self.player.feet.collidelist(self.dragon) > -1:
                        if self.player.feet.collidelist(self.flute) > -1 and self.player.feet.collidelist(
                                self.sword) > -1:
                            self.running = True
                            self.screen.blit(victory, (0, 0))
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    self.running = False

            elif self.status == 2:
                self.screen.blit(game_over, (0, 0))

            else:
                self.screen.blit(home_screen, (0, 0))
                self.screen.blit(play_button, (0, 0))

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()
