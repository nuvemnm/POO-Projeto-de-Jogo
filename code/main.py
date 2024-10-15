from config import *
from configs import Configs
from jogador import Jogador
from sprite import *
from pytmx.util_pygame import load_pygame
import utils
import os
import json

from random import randint

class Jogo:
    def __init__(self):
        #setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Mage Survivor')
        self.clock = pygame.time.Clock()
        self.menu = True
        self.running = False
        self.configs = utils.loadConfigs()
        #grupo
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        #sprites
        self.player = Jogador((620, 360), self.all_sprites, self.collision_sprites)
        

    def setup(self):
        mapFilePath = os.path.join('..','data','maps','mapa.tmx')
        map = load_pygame(mapFilePath)
        for x, y, image in map.get_layer_by_name('Grama').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

    def run(self):  
        while self.menu:
            dt = self.clock.tick(60) / 1000
            keys = pygame.key.get_pressed()

            #pygame.QUIT signifa clicar no X da tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                elif keys[pygame.K_RETURN]:
                    self.menu = False
                    self.running = True

            #desenha e atualiza o jogo
            self.screen.fill('purple')
            pygame.display.update()
       
        
        while self.running:
            dt = self.clock.tick(60) / 1000

            #pygame.QUIT signifa clicar no X da tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #update
            self.all_sprites.update(dt)

            #desenha e atualiza o jogo
            self.screen.fill('black')
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        
        
        
        
        
        pygame.quit()

print(configs.bigMage)


#jogo = Jogo()
#jogo.run()