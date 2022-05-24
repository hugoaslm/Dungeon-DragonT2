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

        # Charger la carte TILED
        tmx_data = pytmx.util_pygame.load_pygame("Finalee.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Générer le joueur
        self.player = Player()

        # Générer l'inventaire
        self.gui = GUI()
        self.gui_sword = GUI_sword()
        self.gui_flute = GUI_flute()
        self.gui_both = GUI_both()

        # Générer la barre de vie
        self.full_health = full_health()
        self.low_health = low_health()
        self.full_shield_health = full_shield_health()

        # Générer le monstre
        self.skeleton1 = Skeleton1()
        self.skeleton2 = Skeleton2()
        self.skeleton3 = Skeleton3()
        self.dragon_pixel = DragonPixel(1895, 295)
        self.minotaur = Minotaur(640, 256)

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "bnd":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Ile avec les squelettes
        self.isles = []

        for obj in tmx_data.objects:
            if obj.type == "ile":
                self.isles.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Collision coffre contenant l'épée
        self.sword = []

        for obj in tmx_data.objects:
            if obj.type == "sword":
                self.sword.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Collision coffre contenant la flute
        self.flute = []

        for obj in tmx_data.objects:
            if obj.type == "flt":
                self.flute.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Collision coffre contenant le bouclier
        self.shield = []

        for obj in tmx_data.objects:
            if obj.type == "shield":
                self.shield.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Collision coffre contenant la potion de vie
        self.healing = []

        for obj in tmx_data.objects:
            if obj.type == "healing":
                self.healing.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Collision dragon
        self.dragon = []

        for obj in tmx_data.objects:
            if obj.type == "drg":
                self.dragon.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Collision Minotaure
        self.minotaur_isle = []

        for obj in tmx_data.objects:
            if obj.type == "mtr":
                self.minotaur_isle.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=21)
        self.group.add(self.player)
        self.group.add(self.skeleton1)
        self.group.add(self.skeleton2)
        self.group.add(self.skeleton3)
        self.group.add(self.dragon_pixel)
        self.group.add(self.minotaur)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        # Action des touches du clavier
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

        # Ecran Game Over
        game_over = pygame.image.load("MENU/game_over.png")

        # Ecran victoire
        victory = pygame.image.load("MENU/victory.png")

        while self.running:

            # Fermer la fenêtre ferme le jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Lancer le jeu lors du click sur le bouton START GAME
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        self.status = 1

            # Lancement du jeu
            if self.status == 1:
                self.player.save_location()
                self.handle_input()
                self.update()
                self.group.center(self.player.rect.center)
                self.group.draw(self.screen)
                self.full_health.render(self.screen)
                self.gui.render(self.screen)

                # Passer sur le coffre contenant l'épée fait afficher l'inventaire contenant l'épée
                self.swordF = []
                if self.player.feet.collidelist(self.sword) > -1:
                    self.swordF = self.sword
                self.swordF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.sword) > -1:
                    self.gui_sword.render(self.screen)

                    # Si le joueur est déjà passé sur le coffre de la flute, on affiche l'inventaire avec les deux items
                    if self.player.feet.collidelist(self.flute) > -1:
                        self.gui_both.render(self.screen)

                # Passer sur le coffre contenant la flute fait afficher l'inventaire contenant la flute
                self.fluteF = []
                if self.player.feet.collidelist(self.flute) > -1:
                    self.fluteF = self.flute
                self.fluteF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.flute) > -1:
                    self.gui_flute.render(self.screen)

                    # Si le joueur est déjà passé sur le coffre de l'épée, on affiche l'inventaire avec les deux items
                    if self.player.feet.collidelist(self.sword) > -1:
                        self.gui_both.render(self.screen)

                # Passer par l'île des squelettes fait afficher une barre de vie où il manque des points de vie
                self.HF = []
                if self.player.feet.collidelist(self.isles) > -1:
                    self.HF = self.isles
                self.HF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.isles) > -1:
                    self.low_health.render(self.screen)

                    # Si on affronte le minotaure et que nous avons pas la potion de vie, Game Over
                    if self.player.feet.collidelist(self.minotaur_isle) > -1 and not self.player.feet.collidelist(self.healing) > -1:
                        self.game_over()

                    # Si on affronte le minotaure et que nous avons pas la potion de vie, Game Over
                    if self.player.feet.collidelist(self.dragon) > -1 and not self.player.feet.collidelist(self.healing) > -1 :
                        self.game_over()

                # Passer sur le coffre contenant la potion de vie fait afficher la barre de vie pleine
                if self.player.feet.collidelist(self.healing) > -1:
                    self.HF = self.healing
                self.HF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.healing) > -1:
                    self.full_health.render(self.screen)

                    # Si on affronte le minotaure et que nous avons la potion de vie et la flûte, le minotaure s'endort
                    if self.player.feet.collidelist(self.minotaur_isle) > -1:
                        if self.player.feet.collidelist(self.flute) > -1:
                            self.running = True
                        else:
                            self.game_over()

                    # Si on affronte le dragon, barre de vie complète mais que nous avons pas le bouclier, Game Over
                    if self.player.feet.collidelist(self.dragon) > -1 and not self.player.feet.collidelist(self.shield) > -1:
                        self.game_over()

                # Passer sur le coffre contenant le bouclier fait afficher le bouclier complet
                if self.player.feet.collidelist(self.shield) > -1:
                    self.HF = self.shield
                self.HF.append(pygame.Rect(0, 0, 3200, 1600))
                if self.player.feet.collidelist(self.shield) > -1:
                    self.full_shield_health.render(self.screen)

                    # Si on affronte le minotaure, que nous avons la flûte et une barre de vie/bouclier complète, le minotaure s'endort
                    if self.player.feet.collidelist(self.minotaur_isle) > -1:
                        if self.player.feet.collidelist(self.flute) > -1 and not self.player.feet.collidelist(self.healing) > -1:
                            self.running = True

                    # Si on affronte le dragon, barre de vie/bouclier complète et les deux items, VICTOIRE !
                    if self.player.feet.collidelist(self.dragon) > -1:
                        if self.player.feet.collidelist(self.flute) > -1 and self.player.feet.collidelist(
                                self.sword) > -1:
                            self.running = True
                            self.screen.blit(victory, (0, 0))

                            # Fermer la fenêtre ferme le jeu
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    self.running = False

            elif self.status == 2:
                # Affiche l'écran "Game Over"
                self.screen.blit(game_over, (0, 0))

            else:

                # Status par défaut = écran d'accueil
                # Affichage de l'écran d'acceuil et du bouton "Start Game"
                self.screen.blit(home_screen, (0, 0))
                self.screen.blit(play_button, (0, 0))

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()