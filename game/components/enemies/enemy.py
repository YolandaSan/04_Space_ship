import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    Y_POS = 20
    X_POS_LIST =[50,100,150,200,250,300,350,400,450,500,550]
    SPEED_X = 5
    SPEED_Y = 1
    MOD_X = {0:'left', 1:'right'}
    # Se agregó al metodo contructor, el parametro Imagen
    def __init__(self, image):
        # Se asigna la imagen que nos llega por parametros
        self.image = image
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0,10)]
        self.rect.y = self.Y_POS
        self.type = 'enemy'

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOD_X[random.randint(0,1)]
        self.move_x_for = random.randint(30,100)
        self.index = 0
        self.shooting_time = random.randint(30,50)


    def change_movement_x(self):
        self.index +=1
        if(self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH -40 ):
           self.movement_x = 'left'
        elif(self.index >=self.move_x_for and self.move_x_for == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'

        if self.index >=self.move_x_for:
            self.index = 0


    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()
        if self.rect.y >= SCREEN_HEIGHT:
           ships.remove(self)

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(20,50)

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
