import pygame
#definir une classe pour les anims

class AnimateSprite(pygame.sprite.Sprite):
    
    #definir les choses à faire à la création de l'entité
    def __init__(self,sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 #commencer a l'img 0
        self.images = animations.get(sprite_name)
        self.animation = False
        
    #definir une méthode pour démarrer l'anim
    def start_animation(self):
        self.animation = True
        
        
    #definir une méthode pour animer les sprites
    def animate(self, loop=False):
        
        #vérifier si l'anim est active
        if self.animation:
            
            
            #passer a l'img suivante
            self.current_image += 1
            
            if self.current_image >= len(self.images):
                #remettre l'anim au départ
                self.current_image = 0
                
                #vérifier si l'anim n'est pas en boucle
                if loop is False:
                    #désactiver l'anim
                    self.animation = False
                
                #modifier l'image de précedente par la suivante
            self.image = self.images[self.current_image]
        
        
    #definir une fonctions pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images du sprite
    images = []
    #recup les chemin du dossier pour le sprite
    path = f"assets/{sprite_name}/{sprite_name}"
        
    #boucler sur chaque fichiers chaque image
        
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
           
        #renvoyer le contenu de la liste d'images
    return images
    
    # definir un dictionnaire qui va contenir les imgs chargées 

animations = {
    'mummy' : load_animation_images('mummy'),
    'player': load_animation_images('player')
}