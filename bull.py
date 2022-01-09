import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """ Инициализация пули """
        super(Bullet, self).__init__()
        self.screen = screen #подзагрузили экран
        self.rect = pygame.Rect(0, 0, 2, 8) #отрисовывоем пулю, где появляеться и размер
        self.color = (76, 175, 79) #цвет пули
        self.speed = 4.5 #скорость пули
        self.rect.centerx = gun.rect.centerx #появление пули в пушке
        self.rect.top = gun.rect.top #в верхней части пушки
        self.y = float(self.rect.y) #указываем что пуля будет двигвться в верх

    def update(self):
        """ Перемещение пули """
        self.y -= self.speed #указываем что она перемещиеться в вверх
        self.rect.y = self.y #обновление позиции

    def draw_bullet(self):
        """ Отрисовка пули"""
        pygame.draw.rect(self.screen, self.color, self.rect) #где, кокого цвета, размер