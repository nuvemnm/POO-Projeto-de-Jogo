from config import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, posicao: int, grupo):
        super().__init__(grupo) 
        self.image = pygame.image.load('C:/UFMG/02-2024/POO/POO-Projeto-de-Jogo/images/personagem/magomenor.png').convert_alpha()
        self.rect = self.image.get_rect(center = posicao)

        self.direction = pygame.Vector2()
        self.speed = 500

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        if keys[pygame.K_RIGHT]:
            self.image = pygame.image.load('C:/UFMG/02-2024/POO/POO-Projeto-de-Jogo/images/personagem/magomenor-direita.png').convert_alpha()
        elif keys[pygame.K_LEFT]:
            self.image = pygame.image.load('C:/UFMG/02-2024/POO/POO-Projeto-de-Jogo/images/personagem/magomenor.png').convert_alpha()

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt 

    def update(self, dt):
        self.input()
        self.move(dt)