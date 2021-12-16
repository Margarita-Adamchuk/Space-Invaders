import pygame
import sys
from bull import Bullet

def events(screen, gun, bullets):
    """ Обработка действий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: # Вправо
                gun.mright = True
            elif event.key == pygame.K_a: # Влево
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d: # Вправо
                gun.mright = False
            elif event.key == pygame.K_a: # Влево
                gun.mleft = False

def update(bg_color, screen, gun, bullets):
    """ Обновление экрана """
    screen.fill(bg_color)
    for bull in bullets.sprites():
        bull.draw_bullet()
    gun.output()
    pygame.display.flip()

def update_bullets(bullets):
    """ Обновление позиции пули, удаляе те что уже вышли за предел экрана """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)