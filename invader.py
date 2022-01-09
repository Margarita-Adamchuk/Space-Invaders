import pygame
import random

class Invader(pygame.sprite.Sprite):
    """ Класс пришельцев"""

    def __init__(self, screen):
        """ Инициализация и начальная позиция """
        one = ["pixilart fail/2,2.png", "pixilart fail/2,1.png", "pixilart fail/2,3.png", "pixilart fail/2,0.png", "pixilart fail/1,3.png"
               , "pixilart fail/1,2.png", "pixilart fail/1,1.png", "pixilart fail/1,0.png", "pixilart fail/3,0.png", "pixilart fail/3,1.png"
               , "pixilart fail/3,2.png"]
        super(Invader, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(random.choice(one))
        self.rect = self.image.get_rect() #создаем пришельца в виде прямоугольника
        self.rect.x = self.rect.width #помещаем его в левый угол
        self.rect.y = self.rect.height #в верхний левый угол
        self.x = float(self.rect.x) #прописываем координаты тк пришельцы будут перемещаться
        self.y = float(self.rect.y)

    def draw(self):
        """ Отрисовка пришельца """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Перемещение пришельцев """
        self.y += 0.1
        self.rect.y = self.y