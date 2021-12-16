import pygame

class Gun():

    def __init__(self, screen):
        """ Инициализация пушки """
        self.screen = screen
        self.image = pygame.image.load('pixilart fail/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False # вправо
        self.mleft = False # влево

    def output(self):
        """ Отрисовка пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """ Обновление позиции пушки """
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.2
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.2

        self.rect.centerx = self.center