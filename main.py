import pygame
from pygame.constants import K_LEFT
from game import Game
pygame.init()

#Creer une classe pour le jeu 




#generer la fenetre
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1080,720))



#importer le background 
background = pygame.image.load("assets/bg.jpg")

#charger le jeu 

game = Game()




running = True
#boucle de jeu 

while running:
    #appliquer l'arriere plan 
    screen.blit(background,(0,-200))
    
    #appliquer l'img du joueur 
    
    screen.blit(game.player.image, game.player.rect)
    
    #verifier la direction du joueur
    
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        
    
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
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
           