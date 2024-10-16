import os
from os.path import join
from config import *
from jogador import Jogador
from sprite import *
from pytmx.util_pygame import load_pygame
from groups import AllSprites

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

        #grupo
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        #sprites
        
        

    def setup(self):
        map_path = os.path.abspath(join('maps', 'mapa.tmx'))
        map = load_pygame(map_path)
        for x, y, image in map.get_layer_by_name("Grama").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("Parede").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("SecondFloor").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("Objects").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("Objects2").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("Details").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)


        for obj in map.get_layer_by_name('collision'):
            collision((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'player':
                self.player = Jogador((obj.x, obj.y), self.all_sprites, self.collision_sprites)

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
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
        
        
        
        
        
        pygame.quit()


jogo = Jogo()
jogo.run()