import pygame
import event
from gun_game import Gun
from pygame.sprite import Group
from stats import Ststs
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800)) #создаем окно
    pygame.display.set_caption("Первая игра") #название игры
    bg_color = (0, 0, 0) #фоновый цвет
    gun = Gun(screen) #создаем обьект пушки
    bullets = Group() #создаем группу пуль
    inos = Group() #создаем группу иноплонетян
    event.create_army(screen, inos) #функция которая создает армию из группы пришельцев
    stats = Ststs() #статистика
    sc = Scores(screen, stats) #создаем экземпляр счета

    while True:
        event.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun() #обновляет позицию пушки
            event.update(bg_color, screen, stats, sc, gun, inos, bullets)
            event.update_bullets(screen, stats, sc, inos, bullets)
            event.update_inos(stats, screen, sc, gun, inos, bullets)


run()