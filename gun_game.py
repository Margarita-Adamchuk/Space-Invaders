import pygame

class Gun():

    def __init__(self, screen):
        """ Инициализация пушки """
        self.screen = screen #получаем экран
        self.image = pygame.image.load('pixilart fail/gun.png') #загружаем изображение из папки
        self.rect = self.image.get_rect() #преобразовываем нашу картинку как прямоугольник
        self.screen_rect = screen.get_rect() #получаем обьек экрана как прямоугольк
        self.rect.centerx = self.screen_rect.centerx #координаты пушки, по центру
        self.center = float(self.rect.centerx) #переводи в дробь для более плавного движения
        self.rect.bottom = self.screen_rect.bottom #координато низа пушки
        self.mright = False # движение вправо
        self.mleft = False # движение влево

    def output(self):
        """ Отрисовка пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """ Обновление позиции пушки """
        if self.mright and self.rect.right < self.screen_rect.right: #проверка не выходит ли пушка за экран
            self.center += 2.8 #шаг пушки
        elif self.mleft and self.rect.left > 0: #проверка не выходит ли пушка за экран
            self.center -= 2.8 #шаг пушки

        self.rect.centerx = self.center

    def create_gun(self):
        """ Размещает пушку по центру """
        self.center = self.screen_rect.centerx