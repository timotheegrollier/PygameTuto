import pygame
from comet import Comet

# créer une classe pour gérer cet evenement

class CometFallEvent:
    #lors du chargement -> créer un compteur
    
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        
        # definir un groupe de spritte pour les cometes
        self.all_comets = pygame.sprite.Group()
        
        
    def add_percent(self):
        self.percent += self.percent_speed/100
        
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
            self.percent = 0
        
    def meteor_fall(self):
        # boucle pour les comets
        for i in range(1,10):
        # apparaitre 1 boule de feu
            self.all_comets.add(Comet(self))
        

    
    
    def attempt_fall(self):
        # la jauge est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True # activer l'event
            
        
        
    def update_bar(self,surface):
        #ajouter du pourcentage à la barre
        self.add_percent()
        

        
        # barre noir (arriere plan)
        pygame.draw.rect(surface, (187,11,11),[0,surface.get_height() -20,surface.get_width(),10 ])
        #barre rouge (event)
        pygame.draw.rect(surface, (0,0,0),[0,surface.get_height() -20,(surface.get_width() / 100) * self.percent,10 ])
 