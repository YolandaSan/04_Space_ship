import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET,BULLET_ENEMY,SCREEN_HEIGHT

class Bullet(Sprite):
    X_POS = 80
    Y_POS = 30
    SPEED = 20
    BULLET_SIZE = pygame.transform.scale(BULLET,(10,20))
    BULLET_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY, (9,32))
    ## Creamos un diccionario con tipos de nave, que define el 
    ## tamaño de la bala dependiendo de la nave
    BULLETS = {'player':BULLET_SIZE, 'enemy':BULLET_SIZE_ENEMY}


    def __init__(self,spaceship):
        ## Dependiendo del tipo de nave que me llegue
        ## obtengo uno u otro valor
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type


    def events(self):
        pass

    def update(self, bullets):
        ## Se crea una condicion donde se valida el tipo de nave
        if self.owner == 'enemy':
            ## si la nave es enemiga, el disparo va de arriba hacia abajo
            ## se va sumando de en 20
            self.rect.y += self.SPEED
            ## Si self.rect.y es mayor oigual a 600
            if self.rect.y >= SCREEN_HEIGHT:
                ## Removemos de la lista el objeto bullet
                ## Es decir, elimina el disparo cuando se sale del borde de la pantalla
                bullets.remove(self)
        else:
            ## Si la nave es player , el disparo va de abajo hacia arriba
            ## se va restando de 20 en 20
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                ## Removemos de la lista el objeto bullet 
                ## Es decir, elimina el disparo cuando llega a 0 ya que sale del 
                ## borde de la pantalla
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

