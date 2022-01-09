import pygame
import sys
from bull import Bullet
from invader import Invader
import time

def events(screen, gun, bullets):
    """ Обработка действий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #прверка на нажатие клавиши
            if event.key == pygame.K_RIGHT: # Вправо
                gun.mright = True
            elif event.key == pygame.K_LEFT: # Влево
                gun.mleft = True
            elif event.key == pygame.K_SPACE: # пробел, вылетает пуля
                new_bullet = Bullet(screen, gun) #создаем пулю
                bullets.add(new_bullet) #добавляем его в группу
        elif event.type == pygame.KEYUP: #клавиша отжата
            if event.key == pygame.K_RIGHT: # Вправо
                gun.mright = False
            elif event.key == pygame.K_LEFT: # Влево
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, inos,  bullets):
    """ Обновление экрана """
    screen.fill(bg_color) #фон экрана
    sc.show_score() #отрисовываем счет
    for bull in bullets.sprites(): #для пули в нашем контейнере
        bull.draw_bullet() #создаю и отрисовываю
    gun.output() #отрисовка пушки
    inos.draw(screen) #отрисовывает иноплонетянина
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    """ Обновление позиции пули, удаляе те что уже вышли за предел экрана """
    bullets.update() #вызываем метод перемещения
    for bullet in bullets.copy(): #для пули в нашем скопировонном контейнере
        if bullet.rect.bottom <= 0:  #если низ пули вышел за пределы экрана
            bullets.remove(bullet) #удаляем ее из контейнера
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos) #увеличиваем счет на 10 если убили 1 пришельца
        sc.image_score() #отрисовываем новый счет если он поменялся
        check_max_score(stats, sc)
        sc.image_lifs() #выводим количество жизней
    if len(inos) == 0: #если мы удалии всех пришельцев
        bullets.empty() #удаляем все пули
        create_army(screen, inos) #создаем новую армию

def update_inos(stats, bg_color, screen, sc, gun, inos, bullets):
    """ Обновление позиции пришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, bg_color, screen, sc, gun, inos, bullets)
    inos_check(stats, bg_color, screen, sc, gun, inos, bullets)

def inos_check(stats, bg_color, screen, sc, gun, inos, bullets):
    """ Проверка добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom: #если нижняя позиция приш. больше позиции экрана
            gun_kill(stats, bg_color, screen, sc, gun, inos, bullets)
            break

def create_army(screen, inos):
    """Создание группы пришельцев"""
    ino = Invader(screen)
    ino_width = ino.rect.width #ширина
    ino_height = ino.rect.height #высота

    for row_number in range(14):
        for ino_number in range(12):
            ino = Invader(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino) #добавление в группу

def gun_kill(stats, bg_color, screen, sc, gun, inos, bullets):
    """ Пришельцы достигли пушки """
    if stats.guns_left > 0:
        stats.guns_left -= 1 #удаляем жизнь
        sc.image_lifs() #отрисовка жизней
        inos.empty() #очищаем экран от пришельцев
        bullets.empty() #очищанм пули с экрана
        create_army(screen, inos) #создаем заново армию пришельцев
        gun.create_gun() #отрисовываем заново пушку после ее уничтожения
        time.sleep(1) #время перезагрузки
    else:
        stats.run_game = False
        update_game_over(bg_color, screen, sc, gun)
        time.sleep(2)
        sys.exit() # выход из игры

def check_max_score(stats,  sc):
    """ Проверка новых рекордов """
    if stats.score > stats.max_score:
        stats.max_score = stats.score
        sc.image_max_score() #отрисовываем рекорд
        with open('max_score', 'w') as fill:
            fill.write(str(stats.max_score)) #запись рекорда в фаил

def update_game_over(bg_color, screen, sc, gun):
    """ Обновление экрана """
    screen.fill(bg_color) #фон экрана
    sc.show_score() #отрисовываем счет
    sc.show_score_gameOver()
    gun.output() #отрисовка пушки
    pygame.display.flip()