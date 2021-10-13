import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

class Game:
    
    def __init__(self):
        # definir si le jeu a commencé 
        self.is_playing = False
        #generer le joeueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'event
        self.comet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        
        
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

        
        
        
    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres remmetre le jpoueur a 100 et jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        # reset les projectiles
        self.player.all_projectiles = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.is_playing = False
        
        
        
    def update(self,screen):
        
    #appliquer l'img du joueur 
        screen.blit(self.player.image, self.player.rect)
    
    #actualiser la barre de vie du joueur
    
        self.player.update_health_bar(screen)
        
        
    #actualiser la barre d'évent du jeu
    
        self.comet_event.update_bar(screen)
    
    
        #recup les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
            
            #recup les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            
            
            #recup les comets
        for comet in self.comet_event.all_comets:
            comet.fall()
        
        #appliquer le groupe projectile
        self.player.all_projectiles.draw(screen)
        
        #aplliquer le groupe de monstres
        self.all_monsters.draw(screen)
        
        #appliquer le groupe de cometes
        self.comet_event.all_comets.draw(screen)
    
    #verifier la direction du joueur
        
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        
        
        
        
    def check_collision(self,sprite , group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
        
        

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
