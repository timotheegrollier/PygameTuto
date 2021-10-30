import pygame
import math
from pygame.constants import K_LEFT
from game import Game
pygame.init()

#Creer une classe pour le jeu 

# definir une clock
clock = pygame.time.Clock()
FPS = 140


#generer la fenetre
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1080,720))



#importer le background 
background = pygame.image.load("assets/bg.jpg")

#importer charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)


# Importer le bouton de lancement
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() /2)

#charger le jeu 

game = Game()




running = True
#boucle de jeu 

while running:
    
    #appliquer l'arriere plan 
    screen.blit(background,(0,-200))
    
   #verifier si le jeu à commencé 
    if game.is_playing:
       # declencher les instructions de la partie
        game.update(screen)
        #verifier si le jeu n'a pas commencé 
    else:
        screen.blit(play_button,(play_button_rect))
        screen.blit(banner,(banner_rect))
    
    
    #mettre a jour le screen
    pygame.display.flip()
    
    
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'vent est fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture")
        #detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #detecter si la touche espace est enfoncée
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.lauch_projectile()
                else:
                    game.start()
                #jouer le son
                    game.sound_manager.play('click')
                    
                
                
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton
            if play_button_rect.collidepoint(event.pos):
                game.start()
                #jouer le son
                game.sound_manager.play('click')
    clock.tick(FPS)