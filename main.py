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
    
    #recup les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
        
        #recup les monstres
    for monster in game.all_monsters:
        monster.forward()
    
    #appliquer le groupe projectile
    game.player.all_projectiles.draw(screen)
    
    #aplliquer le groupe de monstres
    game.all_monsters.draw(screen)
    
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
            
            #detecter si la touche espace est enfoncée
            if event.key == pygame.K_SPACE:
                game.player.lauch_projectile()
                
                
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
           