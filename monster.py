import pygame
import random
import animation


# crée une classe qui va gérer la notion de monstre sur notre jeu

class Monster(animation.AnimateSprite):
    
    def __init__(self,game, name,size, offset=0):
        super().__init__(name,size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()
        
    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity = random.randint(1,2)
        
    def set_loot_amount(self,amount):
        self.loot_amount = amount
 
        
    def damage(self, amount):
        #infliger les degats
        self.health -= amount
        
        #verifier si son nouveau nombre de PV est inférieur ou égal a 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,self.default_speed)
            self.health = self.max_health
            #ajouter le nombre de points
            self.game.add_score(self.loot_amount)
            
            # si la barre d'event est charger
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                
        # appel de la méthode pour essayer de declencher l'event
                self.game.comet_event.attempt_fall()
                
                
    def update_animation(self):
        self.animate(loop=True)
        
    def update_health_bar(self,surface):
        
        #dessiner notre barre de vie
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        
        
        
    def forward(self):
        #le deplacement ne se fait que si il n'y a pas de collision 
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity 
            
        else:
            #infliger des dégats(au joueur)
            self.game.player.damage(self.attack)
            
            
#definir une classe pour la momie

class Mummy(Monster):
    
    def __init__(self,game):
        super().__init__(game,"mummy",(130,130))
        self.set_speed(2)
        self.set_loot_amount(20)
        
#definir une classe pour l'alien
class Alien(Monster):
    
    def __init__(self,game):
        super().__init__(game,"alien",(300,300),130)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(80)
        