import pygame
from os.path import join
import json

from configs import Configs

def loadAlphaImage(imagePath : str) -> pygame.Surface:
    pygame.image.load(imagePath).convert_alpha()

def loadConfigs() -> bool:
    global configs
    configs = Configs()
    configs.update(join("..","configs","configs.json"))
    if(configs):
        print("Configurações carregadas.")
    else:
        #Jogar exceção
        print("Não carregou as configs.")