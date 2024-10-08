from config import *

class collision(pygame.sprite.Sprite):
    def __init__(self, position, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('purple')
        self.rect = self.image.get_rect(center = position)