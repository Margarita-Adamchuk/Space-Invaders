import pygame
import event
from gun_game import Gun
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Первая игра")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        event.events(screen, gun, bullets)
        gun.update_gun()
        event.update(bg_color, screen, gun, bullets)
        event.update_bullets(bullets)


run()