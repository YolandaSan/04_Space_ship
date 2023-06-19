import pygame
## Importamos la libreria Random
import random

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_TYPE

from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    X_POS = ( SCREEN_WIDTH // 2 ) - 40
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        ## Se crea una variable llamda tiempo de disparo,donde
        ## le asignamos un valor random entre 30 y 50
        self.shooting_time = random.randint(30,50)
        ## Creamos una variable de tipo de nave
        ## que guarda Player
        self.type = 'player'
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE


    ## Se modifica el metodo update, se le 
    ## agrega el parametro game
    def update(self,user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        ## Se crea la condicion, donde valida que
        ## el User_input sea la tecla espacio 
        elif user_input[pygame.K_SPACE]:
            ## Se llama al metodo disparar,y se
            ## pasa por parametro el objeto bullet_manager
            ## que está dentro del objeto game
            self.shoot(game.bullet_manager)


    def move_left(self):
        if self.rect.left > 0:
            print(str(self.rect.x))
            self.rect.x = self.rect.x - 10
        else: 
            self.rect.x = SCREEN_WIDTH
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x = self.rect.x + 10
        else:
          self.rect.x = 0  
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y = self.rect.y - 10
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y = self.rect.y + 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    ## Se crea el metodo shoot, dentro de la clase Spaceship
    ## Recibe por parametros el bullet_manager
    def shoot(self, bullet_manager):
        ## Se crea la variable con el nombre tiempo actual
        ## a la que se le asigna el valor que devuelve 
        ## pygame.time.get_ticks que es tiempo en milisegundos
        current_time = pygame.time.get_ticks()
        ## Se crea una condicion, que me valida que el 
        ## tiempo de disparo sea menor o igual que el tiempo actual
        if self.shooting_time <= current_time:
            ## Se crea una instancia de la clase Bullet
            bullet = Bullet(self)
            ## Se llama el metodo añadir bullet y se le pasa
            ## como parametro el objeto bullet
            bullet_manager.add_bullet_player(bullet)
            ## Se llama la variable tiempo de disparo y le 
            ## asigna un numero random entre el 20 y el 50
            self.shooting_time += random.randint(20,50)


    def set_image(self, size = (40, 60), image = SPACESHIP):
        self.image = image 
        self.image = pygame.transform.scale(self.image, size)