from config import *
from jogador import Jogador

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
        self.all_sprites = pygame.sprite.Group()

        #sprites
        self.player = Jogador((620, 360), self.all_sprites)

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


jogo = Jogo()
jogo.run()