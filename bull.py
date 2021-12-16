import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """ Инициализация пули """
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 8)
        self.color = (76, 175, 79)
        self.speed = 1.2
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """ Перемещение пули """
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Отрисовка пули"""
        pygame.draw.rect(self.screen, self.color, self.rect)