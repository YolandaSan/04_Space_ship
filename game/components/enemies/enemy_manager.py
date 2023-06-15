from game.components.enemies.enemy import Enemy

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3

class Enemy_manager:

    def __init__(self):
        self.enemies = []
        
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)


    def add_enemy(self):
        # se cambia la condicion, si la cantidad de la lista de
        # enemigos es menor a tres se cumple 
        if len(self.enemies) < 3:
            ## cuando la lista de enemigos sea menor que 1 me añada a la
            ## lista en la ultima posicion la imagen del Enemy_1
            if len(self.enemies) < 1:
               self.add_enemy_img(ENEMY_1)
            ##cuando la lista de enemigos sea menor que 2 me añada a la
            ## lista en la ultima posicion la imagen del Enemy_2
            if len(self.enemies) < 2:
               self.add_enemy_img(ENEMY_2)
            ## cuando la lista de enemigos sea mayor que 3, me añada a la
            ## lista en la ultima posicion el Enemy_3
            if len(self.enemies) < 3:
               self.add_enemy_img(ENEMY_3)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
## Se crea el metodo añadir imagen del enemigo 
    def add_enemy_img(self, image):
        #se crea la instancia enemy de la clase Enemy
        #y se le envia la imagen 
        enemy = Enemy(image)
        # se agrega a la lista de enemigos en la ultima
        # posicion el objeto enemy
        self.enemies.append(enemy)