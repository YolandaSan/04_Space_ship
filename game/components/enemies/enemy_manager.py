from game.components.enemies.enemy import Enemy

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3

class Enemy_manager:

    def __init__(self):
        self.enemies = []
        
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)


    def add_enemy(self):
        if len(self.enemies) < 3:
            if len(self.enemies) < 1:
               self.add_enemy_img(ENEMY_1)
            if len(self.enemies) < 2:
               self.add_enemy_img(ENEMY_2)
            if len(self.enemies) < 3:
               self.add_enemy_img(ENEMY_3)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy_img(self, image):
        enemy = Enemy(image)
        self.enemies.append(enemy)