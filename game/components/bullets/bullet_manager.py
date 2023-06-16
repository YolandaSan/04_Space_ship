import pygame

class Bullet_manager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        ## Se crea la lista de player bullets, que inicia vacia
        self.player_bullets = []

    def update(self, game):

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.death_count += 1
                game.playing = False
                pygame.time.delay(1000)
                break
    ## Creamos un metodo nuevo llamado actualizar jugador, que
    ## recibe por parametro el juego
    def update_player(self, game):
        ## Creamos el ciclo for que recorre la lista bullets del jugador
        for bullet in self.player_bullets:
            ## Llamamos el metodo actualizar del bullet y le 
            ## pasamos la lista de bullets del jugador
            bullet.update(self.player_bullets)
            
          ## Creamos una condicion 
          ## 1. validamos que la lista de enemigos sea siempre mayor o igual a 3, por que en caso de no ser asi
          ## nos genera el error de que estamos intentando acceder a una posición en la lista que no existe 
          ## estos nos pasaba cuando las naves enemigas salian de la pantalla para volver a empezar arriba generaba error
          ## 2. validamos que el tipo de nave sea jugador 
            if self.valid_list_enemy_existy(game.enemy_manager.enemies) and bullet.owner == 'player':
                ## validamos que cuando el disparo de la nave del jugador colicione con la nave enemiga en la posicion cero 
                if bullet.rect.colliderect(game.enemy_manager.enemies[0].rect) :
                    ## entonces desaparecemos la la nave enemiga 
                    ## con el metodo pop pasandole la posición de la nave decimos que nave queremos eliminar
                    ## de la lista enemies
                    game.enemy_manager.enemies.pop(0)
                    game.update_score()
                    self.player_bullets.remove(bullet)
                elif bullet.rect.colliderect(game.enemy_manager.enemies[1].rect) :
                    game.enemy_manager.enemies.pop(1)
                    game.update_score()
                    self.player_bullets.remove(bullet)
                elif bullet.rect.colliderect(game.enemy_manager.enemies[2].rect) :
                    game.enemy_manager.enemies.pop(2)
                    game.update_score()
                    self.player_bullets.remove(bullet)
         
            

     ## Creamos el metodo validar lista del enemigo existente, que recibe 
     ## por parametro los enemigos
    def valid_list_enemy_existy(self, enemies):
        ## Valida que la lista de enemigos sea mayor o igual a tres
        if len(enemies) >= 3:
            return True
        return False


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
    
    ## se crea el metodo dibujar del jugador
    def draw_player(self, screen):
        ## se recorre la lista de player bullets
        for bullet in self.player_bullets:
            ## se empieza a dibujar 
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if  bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

    ## se crea el metodo añadir bullet del jugador
    def add_bullet_player(self, bullet):
        ## validamos que el tipo de nave sea plater y que lista de player bullet debe ser menor a cero
        ## si camnbiamos ese numero a 2 o 3 vamos a poder hacer 2 o 3 disparos
        if  bullet.owner == 'player' and len(self.player_bullets) < 1:
            ## se llena lista con bullet
            self.player_bullets.append(bullet)
