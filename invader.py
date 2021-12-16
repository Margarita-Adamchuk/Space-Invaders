import pygame
import random

class Invader(pygame.sprite.Sprite):
    """ Класс пришельцев"""

    two = ['2,0', '2,1', '2,2', '2,3']
    three = ['3,0', '3,1', '3,2']

    def __init__(self, screen):
        """ Инициализация и начальная позиция """
        one = ['1,0', '1,1', '1,2', '1,3']
        super(Invader, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(f"'pixilated fail/{random.choice(one)}.png'")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)