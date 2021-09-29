import pygame
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
    
    #mettre a jour le screen
    pygame.display.flip()
    
    
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'vent est fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture")