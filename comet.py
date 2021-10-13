import pygame
import random

#creer une classe pour gérer la comete
class Comet(pygame.sprite.Sprite):
    
    def __init__(self,comet_event):
        super().__init__()
        # definir l'img
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,800)
        self.comet_event = comet_event
        
        
    def remove(self):
        self.comet_event.all_comets.remove(self)
        
        #verifier si le nombre de comets est de 0
        if len(self.comet_event.all_comets) == 0:
            #remettre la barre a 0
            self.comet_event.reset_percent()
            #apparaitre les 2 premiers monstre
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
        
        
    def fall(self):
        self.rect.y += self.velocity
        
        # ne tombe pas sur le sol
        
        if self.rect.y >= 530:
            #retirer la boule de feu
            self.remove()
            
            # si il n'y a plus de boules de feu
            if len(self.comet_event.all_comets) == 0:
                #remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
            
        #verifier si la boule touche le joueur 
        if self.comet_event.game.check_collision(self,self.comet_event.game.all_players):
            # retirer la boule
            self.remove()
            # subir des dégats
            self.comet_event.game.player.damage(14)