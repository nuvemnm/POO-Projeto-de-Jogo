from config import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Mage Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):  
        while self.running:
            dt = self.clock.tick() / 1000

            #pygame.QUIT signifa clicar no X da tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #atualiza a tela trocando a atual pela gerada em segundo plano
            pygame.display.update()
        
        
        
        
        
        pygame.quit()


jogo = Jogo()
jogo.run()