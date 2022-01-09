import pygame

class Life(pygame.sprite.Sprite):
    """ Инициализация жизней """
    def __init__(self, screen):
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('pixilart fail/life.png')
        self.rect = self.image.get_rect()
        self.x = self.rect.x # прописываем координаты
        self.y = self.rect.y

    def output(self):
        """ Отрисовка жизней """
        self.screen.blit(self.image, self.rect)
