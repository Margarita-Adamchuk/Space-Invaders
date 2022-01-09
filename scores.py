import pygame.font #для помещения текста
from gun_game import Gun #?
from pygame.sprite import Group
from life import Life

class Scores():
    """ Вывод игровой информации """
    def __init__(self, screen, stats):
        """ Инициализация очков """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (76, 175, 79) #цвет шрифта
        self.font = pygame.font.SysFont(None, 38) #вид шрифта и размер
        self.font_game_over = pygame.font.SysFont(None, 150)
        self.image_score()
        self.image_max_score()
        self.image_lifs()
        self.gameOver()

    def image_score(self):
        """ Преобразовывает текст счета в графтческое изображение """
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0)) #рендорим текст в изображение, в строку, цвет, и на фон
        self.score_rect = self.score_img.get_rect() #преобразовываем его в прямоугольник
        self.score_rect.right = self.screen_rect.right - 40 #размещение от правого края экрана
        self.score_rect.top = 20 #отступ от верхней части экрана

    def image_max_score(self):
        """ Рекорд в графическое изображение """
        self.max_score_image = self.font.render(str(self.stats.max_score), True, self.text_color, (0, 0, 0))
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.centerx = self.screen_rect.centerx #находиться по центру
        self.max_score_rect.top = self.screen_rect.top + 20

    def image_lifs(self):
        """ Количество жизней """
        self.lifs = Group()
        for life_number in range(self.stats.guns_left):
            life = Life(self.screen)
            life.rect.x = 5 + life_number * life.rect.width
            life.rect.y = 10
            self.lifs.add(life)

    def gameOver(self):
        """ надпись при проигрыше """
        self.gameOver_image = self.font_game_over.render(str(self.stats.game_over), True, self.text_color, (0, 0, 0))
        self.gameOver_rect = self.gameOver_image.get_rect()
        self.gameOver_rect.centerx = self.screen_rect.centerx  # находиться по центру
        self.gameOver_rect.top = self.screen_rect.top + 200


    def show_score(self):
        """ Отрисовываем счет на экране """
        self.screen.blit(self.score_img, self.score_rect) #отрисовываем текущий счет
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.lifs.draw(self.screen)

    def show_score_gameOver(self):
        """ Оирсовка последней надписи """
        self.screen.blit(self.gameOver_image, self.gameOver_rect)

